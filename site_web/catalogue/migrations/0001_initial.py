# Generated by Django 5.1.3 on 2024-11-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Species",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                (
                    "name_leaf",
                    models.CharField(blank=True, max_length=200, unique=True),
                ),
                (
                    "name_fruit",
                    models.CharField(blank=True, max_length=200, unique=True),
                ),
                (
                    "file_leaf",
                    models.CharField(blank=True, max_length=200, unique=True),
                ),
                (
                    "file_fruit",
                    models.CharField(blank=True, max_length=200, unique=True),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=100000, unique=True),
                ),
                (
                    "folder_gallery",
                    models.CharField(blank=True, max_length=200, unique=True),
                ),
                ("keywords", models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
