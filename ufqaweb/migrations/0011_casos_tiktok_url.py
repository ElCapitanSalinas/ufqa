# Generated by Django 5.0.6 on 2024-06-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufqaweb', '0010_casos_last_update_casos_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='casos',
            name='tiktok_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]