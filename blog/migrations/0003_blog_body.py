# Generated by Django 3.0.7 on 2020-07-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200708_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
