# Generated by Django 4.0.4 on 2022-05-14 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sDogAPIApp', '0002_alter_dog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='dog_img/'),
        ),
    ]
