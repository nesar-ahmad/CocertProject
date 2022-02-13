# Generated by Django 4.0 on 2022-01-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_options_profile_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], default=1, verbose_name='جنسیت'),
        ),
    ]
