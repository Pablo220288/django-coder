# Generated by Django 5.0.6 on 2024-07-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('testimonial', models.TextField(default='')),
                ('image_url', models.CharField(default='', max_length=2083)),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
