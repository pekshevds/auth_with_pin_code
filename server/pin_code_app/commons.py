from django.utils import timezone
import datetime
from random import randrange


def default_pin_code():
    return str(randrange(100000, 999999))


def default_date():
    return timezone.now()


def default_date_plus_five_min():
    return timezone.now() + datetime.timedelta(minutes=5)
