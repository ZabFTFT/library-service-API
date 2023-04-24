# Generated by Django 4.2 on 2023-04-24 12:09

import customers_service.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customer",
            managers=[
                ("objects", customers_service.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="customer",
            name="username",
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]