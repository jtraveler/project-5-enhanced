from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


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