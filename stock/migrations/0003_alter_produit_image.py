# Generated by Django 5.0.2 on 2024-03-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_magasin_nom_produit_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
