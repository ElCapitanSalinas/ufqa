# Generated by Django 5.0.6 on 2024-06-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ufqaweb', '0007_alter_casos_donadores'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='titulo',
            new_name='project',
        ),
    ]
