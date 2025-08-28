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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, editable=False
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # JPEG versions (existing)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 80}
    )

    # WebP versions (new)
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFill(800, 600)],
        format='WEBP',
        options={'quality': 85}
    )

    image_thumbnail_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='WEBP',
        options={'quality': 80}
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_safe_image_url(self):
        """Return image URL only if file exists, otherwise return
        placeholder"""
        if self.image:
            try:
                if self.image.storage.exists(self.image.name):
                    return self.image.url
            except Exception:
                pass
        return '/media/noimage.png'

    def get_image_url(self):
        """
        Safely get the image URL, with fallback for missing files
        """
        return self.get_safe_image_url()

    def get_webp_url(self):
        """Get WebP image URL with fallback"""
        try:
            if self.image_webp:
                return self.image_webp.url
        except Exception:
            pass
        return self.get_safe_image_url()

    def get_thumbnail_webp_url(self):
        """Get WebP thumbnail URL with fallback"""
        try:
            if self.image_thumbnail_webp:
                return self.image_thumbnail_webp.url
        except Exception:
            pass
        return self.get_safe_image_url()

    def average_rating(self):
        """Calculate average rating from reviews"""
        avg = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return avg if avg else 0

    def review_count(self):
        """Count total reviews"""
        return self.reviews.count()

    def get_primary_image(self):
        """Get the primary image or first image if no primary is set -
        with file checking"""
        # Check ProductImage instances first
        primary = self.images.filter(is_primary=True).first()
        if primary:
            try:
                if (primary.image and
                        primary.image.storage.exists(primary.image.name)):
                    return primary
            except Exception:
                pass

        # Fallback to any existing image
        for image in self.images.all():
            try:
                if (image.image and
                        image.image.storage.exists(image.image.name)):
                    return image
            except Exception:
                continue

        # Fallback to legacy image field if it exists and file is present
        if self.image:
            try:
                if self.image.storage.exists(self.image.name):
                    return self  # Return self so template can access
                    # self.image.url
            except Exception:
                pass

        return None  # No valid images found

    def get_all_images(self):
        """Get all images including the legacy image field - only existing
        files"""
        valid_images = []

        # Check ProductImage instances
        for image in self.images.all():
            try:
                if (image.image and
                        image.image.storage.exists(image.image.name)):
                    valid_images.append(image)
            except Exception:
                continue

        # Include legacy image if it exists and no new images
        if not valid_images and self.image:
            try:
                if self.image.storage.exists(self.image.name):
                    valid_images.append(self)  # Return self as it has the
                    # image property
            except Exception:
                pass

        return valid_images


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

    # JPEG versions (existing)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 80}
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

    # WebP versions (new)
    image_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(800, 800)],
        format='WEBP',
        options={'quality': 85}
    )
    image_thumbnail_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='WEBP',
        options={'quality': 80}
    )
    thumbnail_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='WEBP',
        options={'quality': 80}
    )
    image_medium_webp = ImageSpecField(
        source='image',
        processors=[ResizeToFit(800, 800)],
        format='WEBP',
        options={'quality': 85}
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

    def get_safe_image_url(self):
        """Return image URL only if file exists, otherwise return
        placeholder"""
        try:
            if self.image and self.image.storage.exists(self.image.name):
                return self.image.url
        except Exception:
            pass
        return '/media/noimage.png'

    def get_image_url(self):
        """Return image URL with fallback for missing files"""
        return self.get_safe_image_url()

    def get_thumbnail_url(self):
        """Return thumbnail URL with fallback for missing files"""
        try:
            if (self.thumbnail and
                    self.thumbnail.storage.exists(self.thumbnail.name)):
                return self.thumbnail.url
        except Exception:
            pass
        return self.get_safe_image_url()  # Fallback to original image

    def get_webp_url(self):
        """Get WebP image URL with fallback"""
        try:
            if self.image_webp:
                return self.image_webp.url
        except Exception:
            pass
        return self.get_safe_image_url()

    def get_thumbnail_webp_url(self):
        """Get WebP thumbnail URL with fallback"""
        try:
            if self.image_thumbnail_webp:
                return self.image_thumbnail_webp.url
        except Exception:
            pass
        return self.get_safe_image_url()

    def get_medium_webp_url(self):
        """Get WebP medium image URL with fallback"""
        try:
            if self.image_medium_webp:
                return self.image_medium_webp.url
        except Exception:
            pass
        return self.get_safe_image_url()


class Review(models.Model):
    """
    Review model for products
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
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
        return (f'{self.product.name} - {self.user.username} - '
                f'{self.rating} stars')


class Favorite(models.Model):
    """
    Favorite model for wishlist functionality
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favorites'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='favorited_by'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        # Ensure one favorite per user per product
        unique_together = ['user', 'product']

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
