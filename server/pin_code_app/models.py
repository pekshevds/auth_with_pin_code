from django.db import models
from django.utils import timezone
import datetime
from auth_app.models import CustomUser
from random import randrange


def default_pin_code():
    return str(randrange(100000, 999999))


def default_date():
    return timezone.now()


def default_date_plus_five_min():
    return timezone.now() + datetime.timedelta(minutes=5)
    # datetime.timedelta(0,3)


class Record(models.Model):
    pin_code = models.CharField(max_length=6, default=default_pin_code)
    created_at = models.DateTimeField(default=default_date)
    use_before = models.DateTimeField(default=default_date_plus_five_min)
    used = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pin_code
