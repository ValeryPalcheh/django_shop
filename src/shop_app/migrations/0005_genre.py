# Generated by Django 5.0.6 on 2024-07-10 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_author_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('reference_book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='genres', to='shop_app.reference_book')),
            ],
        ),
    ]
