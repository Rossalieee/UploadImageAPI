# Generated by Django 4.2.6 on 2023-10-12 00:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='original_file',
            field=models.FileField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]
