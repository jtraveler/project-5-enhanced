from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db import models
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Product, Category, Review, Favorite
from .forms import ProductForm, ReviewForm
from django.db.models import Avg

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.select_related('category').prefetch_related(
        'reviews', 'images'
    ).all()

    # Optimize database queries with select_related and prefetch_related
    query = None
    categories = None
    sort = None
    direction = None

    # Get user's favorited products
    favorited_products = []
    if request.user.is_authenticated:
        favorited_products = Favorite.objects.filter(
            user=request.user
        ).values_list('product_id', flat=True)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'rating':
                # Annotate products with average rating from reviews
                products = products.annotate(
                    avg_rating=Avg('reviews__rating')
                )

                # For both ascending and descending, we want nulls
                # (no reviews) last
                products = products.annotate(
                    has_reviews=models.Case(
                        models.When(avg_rating__isnull=True, then=0),
                        default=1,
                        output_field=models.IntegerField()
                    )
                )
                sortkey = 'avg_rating'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc' and sort != 'rating':
                    # Don't add minus for rating
                    sortkey = f'-{sortkey}'

            # Special handling for rating sorting
            if sort == 'rating':
                if direction == 'desc':
                    # For high to low: products with reviews first
                    # (descending), then by rating (descending)
                    products = products.order_by('-has_reviews', '-avg_rating')
                else:
                    # For low to high: products with reviews first,
                    # then by rating (ascending)
                    products = products.order_by('-has_reviews', 'avg_rating')
            else:
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
            )
            products = products.filter(queries)

    # Add pagination - 20 products per page
    paginator = Paginator(products, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': page_obj,  # Use paginated products
        'page_obj': page_obj,  # Add page object for pagination controls
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'favorited_products': favorited_products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    # Optimize database queries
    product = get_object_or_404(
        Product.objects.select_related('category'), pk=product_id
    )
    reviews = product.reviews.select_related('user').all()
    review_count = product.review_count()
    avg_rating = product.average_rating()

    # Check if current user has already reviewed this product
    user_has_reviewed = False
    if request.user.is_authenticated:
        user_has_reviewed = reviews.filter(user=request.user).exists()

    # Check if current user has favorited this product
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = Favorite.objects.filter(
            user=request.user, product=product
        ).exists()

    review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_count': review_count,
        'avg_rating': avg_rating,
        'review_form': review_form,
        'user_has_reviewed': user_has_reviewed,
        'is_favorited': is_favorited,  # Add this to context
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Add a review to a product """

    product = get_object_or_404(Product, pk=product_id)

    # Check if user has already reviewed this product
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.error(request, 'You have already reviewed this product.')
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            try:
                review.save()
                messages.success(
                    request, 'Thank you! Your review has been added.'
                )
            except Exception:
                messages.error(
                    request, 'You have already reviewed this product.'
                )
        else:
            messages.error(
                request,
                'Failed to add review. Please ensure the form is valid.'
            )

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_review(request, product_id, review_id):
    """ Edit a review """

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    # Check if the user owns this review
    if review.user != request.user:
        messages.error(request, 'Sorry, you can only edit your own reviews.')
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update review. Please ensure the form is valid.'
            )
    else:
        form = ReviewForm(instance=review)

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'product': product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, review_id):
    """ Delete a review """

    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(Review, pk=review_id)

    # Check if the user owns this review
    if review.user != request.user:
        messages.error(
            request, 'Sorry, you can only delete your own reviews.'
        )
        return redirect(reverse('product_detail', args=[product.id]))

    review.delete()
    messages.success(request, 'Your review has been deleted!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def toggle_favorite(request, product_id):
    """Toggle a product as favorite for the current user"""
    product = get_object_or_404(Product, pk=product_id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        # If it already existed, delete it (toggle off)
        favorite.delete()
        is_favorited = False
    else:
        # If it was created, it's now favorited
        is_favorited = True

    # Check if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Return JSON response for AJAX requests
        return JsonResponse({
            'is_favorited': is_favorited,
            'message': f'{"Added to" if is_favorited else "Removed from"} '
                       f'favorites'
        })

    # For regular requests, redirect back
    messages.success(
        request,
        f'{"Added to" if is_favorited else "Removed from"} favorites'
    )
    # Fixed redirect - use HTTP_REFERER or fall back to product detail
    redirect_url = request.META.get(
        'HTTP_REFERER', reverse('product_detail', args=[product_id])
    )
    return redirect(redirect_url)


@login_required
def wishlist(request):
    """ Display user's favorite products """

    favorites = Favorite.objects.filter(user=request.user).select_related(
        'product'
    ).prefetch_related('product__images')

    context = {
        'favorites': favorites,
    }

    return render(request, 'products/wishlist.html', context)
