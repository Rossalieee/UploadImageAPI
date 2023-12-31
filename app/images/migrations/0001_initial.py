# Generated by Django 4.2.6 on 2023-10-11 18:03

import django.core.validators
from django.db import migrations, models
import images.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expiration_time', models.IntegerField(default=300, validators=[images.validators.validate_expiration_time])),
                ('expiration_datetime', models.DateTimeField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original_file', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])])),
            ],
        ),
        migrations.CreateModel(
            name='ThumbnailSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField(default=0)),
            ],
        ),
    ]
