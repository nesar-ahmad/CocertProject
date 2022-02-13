# Generated by Django 4.0 on 2022-01-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSales', '0007_alter_time_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.CharField(choices=[('start', 'فروش بلیط شروع شده است'), ('end', 'فروش بلیط ختم شده است'), ('cancel', 'فروش بلیط لغو شده است'), ('sales', 'در حال فروش بلیط')], default='sales', max_length=6, verbose_name='وضعیت'),
        ),
    ]
