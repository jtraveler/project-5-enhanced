from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
import os


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        """Calculate average rating from reviews"""
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return avg if avg else 0
        
    def review_count(self):
        """Count total reviews"""
        return self.reviews.count()
    
    def get_primary_image(self):
        """Get the primary image or first image if no primary is set"""
        primary = self.images.filter(is_primary=True).first()
        if primary:
            return primary
        # Fallback to first image
        first_image = self.images.first()
        if first_image:
            return first_image
        # Fallback to legacy image field if it exists
        if self.image:
            return self
        return None
    
    def get_all_images(self):
        """Get all images including the legacy image field"""
        images = list(self.images.all())
        # Include legacy image if it exists and no new images
        if self.image and not images:
            return [self]  # Return self as it has the image property
        return images


class ProductImage(models.Model):
    """
    Model to store multiple images per product
    """
    product = models.ForeignKey(
        Product, 
        related_name='images', 
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='product_images/',
        help_text='Upload product image'
    )
    # Thumbnail for gallery - automatically generated
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 85}
    )
    # Medium size for gallery view
    image_medium = ImageSpecField(
        source='image',
        processors=[ResizeToFit(800, 800)],
        format='JPEG',
        options={'quality': 90}
    )
    alt_text = models.CharField(
        max_length=255, 
        blank=True,
        help_text='Alternative text for image (for SEO and accessibility)'
    )
    is_primary = models.BooleanField(
        default=False,
        help_text='Set as primary image for product listings'
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        
    def __str__(self):
        return f"{self.product.name} - Image {self.order + 1}"
    
    def save(self, *args, **kwargs):
        # Auto-generate alt text if not provided
        if not self.alt_text and self.product:
            self.alt_text = f"{self.product.name} - Image {self.order + 1}"
        
        # Ensure only one primary image per product
        if self.is_primary:
            ProductImage.objects.filter(
                product=self.product, 
                is_primary=True
            ).exclude(pk=self.pk).update(is_primary=False)
        
        super().save(*args, **kwargs)
    
    def get_image_filename(self):
        """Get just the filename without path"""
        return os.path.basename(self.image.name)


class Review(models.Model):
    """
    Review model for products
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        # Ensure one review per user per product
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f'{self.product.name} - {self.user.username} - {self.rating} stars'


class Favorite(models.Model):
    """
    Favorite model for wishlist functionality
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorited_by')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        # Ensure one favorite per user per product
        unique_together = ['user', 'product']
    
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'