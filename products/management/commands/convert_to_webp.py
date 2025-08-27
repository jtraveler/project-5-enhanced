from django.core.management.base import BaseCommand
from products.models import Product, ProductImage
from imagekit.utils import get_field
from django.core.files.storage import default_storage
import os

class Command(BaseCommand):
    help = 'Generate WebP versions for all existing product images'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force regeneration of existing WebP images',
        )

    def handle(self, *args, **options):
        force = options['force']
        
        self.stdout.write('Starting WebP conversion process...')
        
        # Convert Product images (legacy image field)
        products = Product.objects.exclude(image='')
        product_count = 0
        
        for product in products:
            if product.image:
                try:
                    # Check if image file exists
                    if not default_storage.exists(product.image.name):
                        self.stdout.write(
                            self.style.WARNING(f'Image file not found for {product.name}: {product.image.name}')
                        )
                        continue
                    
                    # Generate WebP versions
                    webp_field = get_field(product, 'image_webp')
                    thumbnail_webp_field = get_field(product, 'image_thumbnail_webp')
                    
                    if force or not default_storage.exists(webp_field.name):
                        webp_field.generate()
                        
                    if force or not default_storage.exists(thumbnail_webp_field.name):
                        thumbnail_webp_field.generate()
                    
                    product_count += 1
                    self.stdout.write(f'✓ Converted WebP for Product: {product.name}')
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to convert {product.name}: {str(e)}')
                    )
        
        # Convert ProductImage instances
        product_images = ProductImage.objects.all()
        image_count = 0
        
        for product_image in product_images:
            if product_image.image:
                try:
                    # Check if image file exists
                    if not default_storage.exists(product_image.image.name):
                        self.stdout.write(
                            self.style.WARNING(f'Image file not found for {product_image.product.name}: {product_image.image.name}')
                        )
                        continue
                    
                    # Generate WebP versions
                    webp_field = get_field(product_image, 'image_webp')
                    thumbnail_webp_field = get_field(product_image, 'image_thumbnail_webp')
                    medium_webp_field = get_field(product_image, 'image_medium_webp')
                    thumb_webp_field = get_field(product_image, 'thumbnail_webp')
                    
                    if force or not default_storage.exists(webp_field.name):
                        webp_field.generate()
                        
                    if force or not default_storage.exists(thumbnail_webp_field.name):
                        thumbnail_webp_field.generate()
                        
                    if force or not default_storage.exists(medium_webp_field.name):
                        medium_webp_field.generate()
                        
                    if force or not default_storage.exists(thumb_webp_field.name):
                        thumb_webp_field.generate()
                    
                    image_count += 1
                    self.stdout.write(f'✓ Converted WebP for ProductImage: {product_image.product.name} - Image {product_image.order + 1}')
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to convert ProductImage for {product_image.product.name}: {str(e)}')
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nWebP conversion completed!\n'
                f'Products converted: {product_count}\n'
                f'ProductImages converted: {image_count}'
            )
        )