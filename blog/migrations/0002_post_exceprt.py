# Generated by Django 4.2.13 on 2024-06-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exceprt',
            field=models.TextField(blank=True),
        ),
    ]
