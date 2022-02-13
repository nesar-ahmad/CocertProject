from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    man = 1
    woman = 2
    STATUS_CHOICES = (
        (man, "مرد"),
        (woman, "زن"),
    )
    user = models.OneToOneField(
                                User, verbose_name="کاربری",
                                on_delete=models.CASCADE,
                                related_name="profile")
    gender = models.IntegerField("جنسیت", choices=STATUS_CHOICES, default=man)
    image = models.ImageField("عکس", upload_to="profile_images/", null=True)
    credit = models.IntegerField("اعتبار", default=0)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربرها"
