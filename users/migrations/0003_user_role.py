# Generated by Django 5.0.4 on 2024-05-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='standard', max_length=128),
            preserve_default=False,
        ),
    ]
