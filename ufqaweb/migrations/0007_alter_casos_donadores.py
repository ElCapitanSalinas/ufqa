# Generated by Django 5.0.6 on 2024-06-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufqaweb', '0006_remove_casos_imagesbanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casos',
            name='donadores',
            field=models.CharField(max_length=200, null=True),
        ),
    ]