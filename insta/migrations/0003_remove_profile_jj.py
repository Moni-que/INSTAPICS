# Generated by Django 4.0.5 on 2022-06-08 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_profile_jj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='jj',
        ),
    ]