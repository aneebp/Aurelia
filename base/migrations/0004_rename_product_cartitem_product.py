# Generated by Django 5.1 on 2024-09-19 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_account'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='Product',
            new_name='product',
        ),
    ]