# Generated by Django 5.2 on 2025-05-07 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_lista_hash_value_produtos_hash_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='hash_value',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='hash_value',
        ),
    ]
