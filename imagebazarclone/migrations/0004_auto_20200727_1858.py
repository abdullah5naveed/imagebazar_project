# Generated by Django 3.0.8 on 2020-07-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagebazarclone', '0003_auto_20200727_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='imagebazarclone/images/'),
        ),
    ]
