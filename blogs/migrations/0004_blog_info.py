# Generated by Django 4.1 on 2022-08-26 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blog_featured_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='info',
            field=models.CharField(default='', max_length=40),
        ),
    ]