# Generated by Django 2.2.6 on 2020-02-16 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorites', to='recipebox.Recipe'),
        ),
    ]