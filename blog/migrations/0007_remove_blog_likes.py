# Generated by Django 3.1.8 on 2021-08-11 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_blog_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
    ]
