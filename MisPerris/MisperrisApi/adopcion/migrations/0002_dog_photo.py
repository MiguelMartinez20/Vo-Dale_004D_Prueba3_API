# Generated by Django 2.1.3 on 2018-11-27 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='photo',
            field=models.ImageField(default='dog_image/default-img.png', upload_to='dog_image'),
        ),
    ]
