# Generated by Django 5.1.3 on 2024-11-11 07:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_product_category_alter_product_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]