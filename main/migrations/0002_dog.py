# Generated by Django 5.0.6 on 2024-07-21 20:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(choices=[(1, 'новорожденный щенок'), (2, 'щенок'), (3, 'взрослая собака'), (4, 'старенький пес')], default=2)),
                ('breed', models.TextField(default='дворняга', max_length='200')),
                ('size', models.IntegerField(choices=[(1, 'маленький, от 1 до 10 кг'), (2, 'средний, от 11 до 45 кг'), (3, 'крупный, от 46 до 70 кг'), (4, 'очень крупный, от 71 кг')], default=2)),
                ('color', models.IntegerField(choices=[(1, 'светлый'), (2, 'рыжий'), (3, 'темный')])),
                ('activity', models.TextField(max_length='500')),
                ('relations_with_cats', models.BooleanField(null=True)),
                ('relations_with_dogs', models.BooleanField(null=True)),
                ('relations_with_kids', models.BooleanField(null=True)),
                ('relations_with_adults', models.BooleanField(null=True)),
                ('gender', models.BooleanField(help_text='true - девочка, false - мальчик')),
                ('name', models.TextField(max_length='100')),
                ('address', models.TextField(max_length='100')),
                ('description', models.TextField(max_length='1000')),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
