# Generated by Django 5.1.3 on 2024-11-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='description',
            field=models.CharField(blank=True, max_length=100000),
        ),
        migrations.AlterField(
            model_name='species',
            name='file_fruit',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='file_leaf',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='folder_gallery',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='name_fruit',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='species',
            name='name_leaf',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]