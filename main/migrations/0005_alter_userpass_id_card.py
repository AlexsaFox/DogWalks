# Generated by Django 5.0.6 on 2024-07-23 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_dog_is_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpass',
            name='id_card',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]