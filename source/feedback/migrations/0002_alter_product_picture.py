# Generated by Django 4.0 on 2022-03-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, default='/pictures/product.jpg', null=True, upload_to='pictures/', verbose_name='Картинка'),
        ),
    ]