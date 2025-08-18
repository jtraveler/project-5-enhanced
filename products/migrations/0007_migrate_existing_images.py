from django.db import migrations

def migrate_product_images(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    ProductImage = apps.get_model('products', 'ProductImage')
    
    for product in Product.objects.all():
        if product.image:
            # Check if this product already has images in the new system
            if not product.images.exists():
                # Create a ProductImage from the existing image
                ProductImage.objects.create(
                    product=product,
                    image=product.image,
                    is_primary=True,
                    order=0,
                    alt_text=f"{product.name} - Primary Image"
                )
                print(f"Migrated image for product: {product.name}")

def reverse_migration(apps, schema_editor):
    # We don't want to delete the ProductImages if migration is reversed
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productimage'),
    ]

    operations = [
        migrations.RunPython(migrate_product_images, reverse_migration),
    ]