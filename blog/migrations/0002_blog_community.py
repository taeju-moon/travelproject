# Generated by Django 3.2.2 on 2021-06-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='community',
            field=models.CharField(choices=[('C1', 'Community1'), ('C2', 'Community2'), ('C3', 'Community3')], default='C1', max_length=100),
        ),
    ]
