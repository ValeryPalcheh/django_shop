# Generated by Django 5.0.6 on 2024-07-10 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='number',
            new_name='name',
        ),
    ]
