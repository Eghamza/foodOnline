# Generated by Django 4.1.7 on 2023-09-02 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
