# Generated by Django 5.0.4 on 2024-05-10 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_restaurant_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='delivery_time',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours',
            field=models.CharField(default='10-20', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='opening_hours_weekend',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='domains',
            field=models.ManyToManyField(to='restaurants.restaurantdomain'),
        ),
    ]
