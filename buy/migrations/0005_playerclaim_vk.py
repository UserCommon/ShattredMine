# Generated by Django 3.0.4 on 2020-06-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_playerclaim_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerclaim',
            name='vk',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
