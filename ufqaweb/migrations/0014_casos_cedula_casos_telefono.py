# Generated by Django 5.0.6 on 2024-07-02 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufqaweb', '0013_remove_casos_donadores_donadores'),
    ]

    operations = [
        migrations.AddField(
            model_name='casos',
            name='cedula',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='casos',
            name='telefono',
            field=models.CharField(max_length=200, null=True),
        ),
    ]