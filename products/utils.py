from django.conf import settings
import os

def get_placeholder_image():
    """
    Returns the path to the placeholder image
    """
    # You can customize this path
    placeholder = 'noimage.png'
    return os.path.join(settings.MEDIA_URL, placeholder)

def handle_image_upload(image_file, product, is_primary=False, order=None):
    """
    Handle single image upload for a product
    """
    from .models import ProductImage
    
    if order is None:
        # Get the next order number
        last_image = ProductImage.objects.filter(
            product=product
        ).order_by('-order').first()
        order = (last_image.order + 1) if last_image else 0
    
    product_image = ProductImage.objects.create(
        product=product,
        image=image_file,
        is_primary=is_primary,
        order=order
    )
    
    return product_image