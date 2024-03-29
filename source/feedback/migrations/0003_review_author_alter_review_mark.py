# Generated by Django 4.0 on 2022-03-05 10:58

from django.db import migrations, models
import django.db.models.deletion
import feedback.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('feedback', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='auth.user', verbose_name='Автор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='mark',
            field=models.IntegerField(validators=[feedback.models.MinValueValidator(1), feedback.models.MaxValueValidator(5)], verbose_name='Оценка'),
        ),
    ]
