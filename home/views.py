from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    
    # Get featured products, ordered by featured_order, limited to 10 products
    featured_products = Product.objects.filter(
        featured=True
    ).order_by('featured_order', 'name')[:10]
    
    # Get user's favorited products if authenticated
    favorited_products = []
    if request.user.is_authenticated:
        favorited_products = list(request.user.favorites.values_list('product_id', flat=True))
    
    context = {
        'featured_products': featured_products,
        'favorited_products': favorited_products,
    }

    return render(request, 'home/index.html', context)