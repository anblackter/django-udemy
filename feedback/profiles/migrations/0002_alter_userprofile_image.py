# Generated by Django 4.2.1 on 2023-07-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]