# Generated by Django 3.2.18 on 2023-11-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_imagestorage_image_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sku',
            name='default_image_url',
            field=models.ImageField(blank=True, default='', max_length=200, null=True, upload_to='', verbose_name='商品默认图片'),
        ),
    ]
