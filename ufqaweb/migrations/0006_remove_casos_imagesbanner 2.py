# Generated by Django 5.0.6 on 2024-06-14 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ufqaweb', '0005_remove_casos_images_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casos',
            name='imagesbanner',
        ),
    ]
