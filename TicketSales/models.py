from django.db import models
from django.utils.translation import gettext as _
from jalali_date import datetime2jalali, date2jalali
from accounts.models import Profile


class Concert(models.Model):
    name = models.CharField(_("نام کنسرت"), max_length=100)
    singer_name = models.CharField(_("نام خواننده"), max_length=100)
    length = models.PositiveIntegerField("مدت زمان")
    image = models.ImageField("تصویر", upload_to="concert_images/", null=True)

    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(_("نام سالن"), max_length=100)
    address = models.CharField(_("آدرس"), max_length=254)
    phone = models.CharField(_("شماره تماس"), max_length=13, null=True)
    capacity = models.PositiveIntegerField(_("ظرفیت"))

    class Meta:
        verbose_name = "موقعیت"
        verbose_name_plural = "موقعیت ها"

    def __str__(self):
        return self.name


class Time(models.Model):
    start = 1
    end = 2
    cancel = 3
    sales = 4
    STATUS_CHOICES = (
        (start, "فروش بلیط شروع شده است"),
        (end, "فروش بلیط ختم شده است"),
        (cancel, "فروش بلیط لغو شده است"),
        (sales,  "در حال فروش بلیط"),
    )
    concert = models.ForeignKey(
        to="Concert", verbose_name="کنسرت", related_name="times", on_delete=models.PROTECT)
    location = models.ForeignKey(
        Location, verbose_name="موقعیت", on_delete=models.PROTECT)
    start_date_time = models.DateTimeField(_("ساعت و تاریخ برگزاری کنسرت"),)
    seat = models.PositiveIntegerField("تعداد صندلی", null=True, blank=True)
    status = models.IntegerField(
        _("وضعیت"), choices=STATUS_CHOICES, default=sales)

    class Meta:
        verbose_name = "زمان"
        verbose_name_plural = "زمانها"

    def __str__(self):
        return f"{self.concert} starts in {self.location} at {self.start_date_time}"

    def get_jalali_date(self):
        return datetime2jalali(self.start_date_time)


class Ticket(models.Model):
    profile = models.ForeignKey(
        Profile, verbose_name="نام کاربر", on_delete=models.PROTECT)
    time = models.ForeignKey(
        Time, verbose_name="ساعت برگزاری", on_delete=models.PROTECT)
    name = models.CharField("نام تیکت", max_length=100)
    price = models.PositiveIntegerField("قیمت تیکت")
    image = models.ImageField("تصویر", upload_to="ticket_images/", null=True)

    def __str__(self):
        return f"Ticket info: Profile: {Profile.__str__()} Concert info: {self.Time.__str__()}"
