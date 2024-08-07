# Generated by Django 5.0.6 on 2024-07-21 20:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.IntegerField(help_text='если null - то нельзя выгуливать собаку в одиночку', null=True)),
                ('is_valid_until_1', models.DateTimeField()),
                ('is_valid_until_2', models.DateTimeField(null=True)),
                ('is_valid_until_3', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'волонтёр'), (2, 'куратор')], default=1)),
                ('phone', models.TextField(max_length=20)),
                ('telegram', models.TextField(max_length=200)),
                ('is_validated', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
