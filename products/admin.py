from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Product, Category, ProductImage, Review, Favorite


# Category admin remains the same
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# ProductImage inline admin
class ProductImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'thumbnail_preview', 'alt_text', 'is_primary', 'order')
    readonly_fields = ('thumbnail_preview',)
    
    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.thumbnail.url)
        return "No image"
    thumbnail_preview.short_description = 'Preview'


# Update Product admin
class ProductAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image_count',
        'primary_image_preview',
    )
    
    ordering = ('sku',)
    inlines = [ProductImageInline]
    
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'
    
    def primary_image_preview(self, obj):
        primary_image = obj.get_primary_image()
        if primary_image:
            if hasattr(primary_image, 'thumbnail'):
                return format_html('<img src="{}" width="50" height="50" />', primary_image.thumbnail.url)
            elif hasattr(primary_image, 'image'):
                return format_html('<img src="{}" width="50" height="50" />', primary_image.image.url)
        return "No image"
    primary_image_preview.short_description = 'Primary'


# Review admin remains the same
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


# Favorite admin
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name')
    ordering = ('-created_at',)


# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Favorite, FavoriteAdmin)