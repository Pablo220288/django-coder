# Generated by Django 5.0.6 on 2024-07-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_about_delete_user_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='address',
            new_name='position',
        ),
    ]
