# Generated by Django 4.0 on 2022-01-21 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSales', '0008_alter_time_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش بلیط شروع شده است'), (2, 'فروش بلیط ختم شده است'), (3, 'فروش بلیط لغو شده است'), (4, 'در حال فروش بلیط')], default=4, verbose_name='وضعیت'),
        ),
    ]