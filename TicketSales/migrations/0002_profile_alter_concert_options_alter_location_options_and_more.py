# Generated by Django 4.0 on 2022-01-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('family', models.CharField(max_length=100, verbose_name='نام فامیلی کاربر')),
                ('gender', models.IntegerField(choices=[(1, 'مرد'), (2, 'زن')], default=1, verbose_name='جنسیت')),
                ('image', models.ImageField(null=True, upload_to='profile_images/', verbose_name='تصویر')),
            ],
        ),
        migrations.AlterModelOptions(
            name='concert',
            options={'verbose_name': 'کنسرت', 'verbose_name_plural': 'کنسرت'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'موقعیت', 'verbose_name_plural': 'موقعیت ها'},
        ),
        migrations.AlterModelOptions(
            name='time',
            options={'verbose_name': 'زمان', 'verbose_name_plural': 'زمانها'},
        ),
        migrations.AddField(
            model_name='concert',
            name='image',
            field=models.ImageField(null=True, upload_to='concert_images/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='length',
            field=models.PositiveIntegerField(verbose_name='مدت زمان که طول می کشد'),
        ),
        migrations.AlterField(
            model_name='location',
            name='capacity',
            field=models.PositiveIntegerField(verbose_name='ظرفیت'),
        ),
        migrations.AlterField(
            model_name='time',
            name='concert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.concert', verbose_name='کنسرت'),
        ),
        migrations.AlterField(
            model_name='time',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.location', verbose_name='موقعیت'),
        ),
        migrations.AlterField(
            model_name='time',
            name='status',
            field=models.CharField(choices=[('start', 'فروش بلیط شروع شده است'), ('end', 'فروش بلیط ختم شده است'), ('cancel', 'فروش بلیط لغو شده است'), ('sales', 'در حال فروش بلیط')], default='sales', max_length=6, verbose_name='وضعیت'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام تیکت')),
                ('price', models.PositiveIntegerField(verbose_name='قیمت تیکت')),
                ('image', models.ImageField(null=True, upload_to='ticket_images/', verbose_name='تصویر')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.profile', verbose_name='نام کاربر')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.time', verbose_name='ساعت برگزاری')),
            ],
        ),
    ]
