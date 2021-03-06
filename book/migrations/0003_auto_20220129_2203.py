# Generated by Django 3.2.10 on 2022-01-29 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220129_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.publisher', verbose_name='ناشر'),
        ),
        migrations.AddField(
            model_name='electronicbook',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.publisher', verbose_name='ناشر'),
        ),
        migrations.AddField(
            model_name='physicalbook',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.publisher', verbose_name='ناشر'),
        ),
    ]
