# Generated by Django 5.0.6 on 2024-07-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('image_url', models.CharField(default='', max_length=2083)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
