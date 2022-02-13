# Generated by Django 4.0 on 2022-01-20 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSales', '0004_time_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='times', to='TicketSales.concert', verbose_name='کنسرت'),
        ),
    ]
