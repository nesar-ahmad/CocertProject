# Generated by Django 4.0 on 2022-01-28 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'پروفایل', 'verbose_name_plural': 'پروفایل'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_images/', verbose_name='عکس'),
        ),
    ]
