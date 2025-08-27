from django.core.management.base import BaseCommand
from products.models import Product, ProductImage
from django.core.files.storage import default_storage

class Command(BaseCommand):
    help = 'Generate optimized thumbnails for all existing product images'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force regeneration of existing thumbnails',
        )

    def handle(self, *args, **options):
        force = options['force']
        
        self.stdout.write('Starting image optimization process...')
        
        # Process Product images (legacy image field)
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
                    
                    # Generate thumbnails by accessing the properties
                    # This triggers imagekit to generate the thumbnails
                    if hasattr(product, 'image_thumbnail'):
                        try:
                            _ = product.image_thumbnail.url
                        except:
                            pass
                    
                    # Try to generate WebP if supported (will fail silently if not)
                    if hasattr(product, 'image_webp'):
                        try:
                            _ = product.image_webp.url
                        except:
                            pass
                    
                    if hasattr(product, 'image_thumbnail_webp'):
                        try:
                            _ = product.image_thumbnail_webp.url
                        except:
                            pass
                    
                    product_count += 1
                    self.stdout.write(f'✓ Processed thumbnails for Product: {product.name}')
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to process {product.name}: {str(e)}')
                    )
        
        # Process ProductImage instances
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
                    
                    # Generate thumbnails by accessing the properties
                    thumbnail_fields = [
                        'image_thumbnail', 'thumbnail', 'image_medium',
                        'image_webp', 'image_thumbnail_webp', 'thumbnail_webp', 'image_medium_webp'
                    ]
                    
                    for field_name in thumbnail_fields:
                        if hasattr(product_image, field_name):
                            try:
                                field = getattr(product_image, field_name)
                                if field:
                                    _ = field.url  # This triggers generation
                            except:
                                pass  # Skip WebP if not supported
                    
                    image_count += 1
                    self.stdout.write(f'✓ Processed thumbnails for ProductImage: {product_image.product.name} - Image {product_image.order + 1}')
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'Failed to process ProductImage for {product_image.product.name}: {str(e)}')
                    )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nImage processing completed!\n'
                f'Products processed: {product_count}\n'
                f'ProductImages processed: {image_count}\n'
                f'Note: WebP generation will be skipped if not supported'
            )
        )