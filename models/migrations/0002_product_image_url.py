# Generated by Django 5.0.6 on 2024-06-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]