# Generated by Django 3.2.10 on 2022-02-26 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20220226_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='teller',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='translator',
            name='middle_name',
        ),
    ]
