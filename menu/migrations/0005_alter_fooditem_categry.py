# Generated by Django 4.1.7 on 2023-09-02 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_categry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='categry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fooditems', to='menu.categry'),
        ),
    ]