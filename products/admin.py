from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Product, Category, ProductImage, Review, Favorite


# Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    search_fields = ('name', 'friendly_name')


# ProductImage inline admin
class ProductImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'thumbnail_preview', 'alt_text', 'is_primary', 'order')
    readonly_fields = ('thumbnail_preview',)
    
    def thumbnail_preview(self, obj):
        if obj.image:
            try:
                return format_html('<img src="{}" width="100" height="100" />', obj.get_thumbnail_url())
            except:
                return "No image"
        return "No image"
    thumbnail_preview.short_description = 'Preview'


# Product admin with enhanced search and filtering
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase

class ProductAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image_count',
        'created_at',
        'primary_image_preview',
    )
    
    list_filter = (
        'category',
        'created_at',
        'price',
        'has_sizes',
    )
    
    search_fields = (
        'name',
        'sku',
        'description',
        'category__name',
        'category__friendly_name',
    )
    
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [ProductImageInline]
    
    # Optionally, add list_per_page to control pagination
    list_per_page = 60
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'
    
    def primary_image_preview(self, obj):
        primary_image = obj.get_primary_image()
        if primary_image:
            try:
                # Use the safe get_image_url method
                if hasattr(primary_image, 'get_thumbnail_url'):
                    image_url = primary_image.get_thumbnail_url()
                elif hasattr(primary_image, 'get_image_url'):
                    image_url = primary_image.get_image_url()
                elif hasattr(primary_image, 'image'):
                    # For legacy Product image field
                    image_url = primary_image.get_image_url()
                else:
                    return "No image"
                
                # Make the image clickable with a link to the edit page
                return format_html(
                    '<a href="{}"><img src="{}" width="80" height="80" style="object-fit: cover; border-radius: 4px;" /></a>',
                    f'/admin/products/product/{obj.id}/change/',
                    image_url
                )
            except Exception as e:
                # Handle any unexpected errors
                return "Image error"
        return "No image"
    primary_image_preview.short_description = 'Image'


# Review admin
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'created_at',
    )
    list_filter = (
        'rating',
        'created_at',
    )
    search_fields = (
        'product__name',
        'user__username',
        'comment',
    )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'


# Favorite admin
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'


# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)