# Generated by Django 4.0 on 2023-10-20 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(default=1, upload_to='subcategory'),
            preserve_default=False,
        ),
    ]