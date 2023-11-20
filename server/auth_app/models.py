from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    password = models.CharField(
        _("password"),
        max_length=128,
        default=make_password(settings.AUTH_USER_DEFAULT_PASSWORD)
    )
