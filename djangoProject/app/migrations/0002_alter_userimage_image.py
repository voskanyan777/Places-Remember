# Generated by Django 5.0.6 on 2024-05-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.TextField(verbose_name='ссылка на изображение'),
        ),
    ]