# Generated by Django 4.2.3 on 2023-08-06 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
