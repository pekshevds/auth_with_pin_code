from django.db import models
from auth_app.models import CustomUser
from pin_code_app.commons import (
    default_date_plus_five_min,
    default_date,
    default_pin_code
)


class Record(models.Model):
    pin_code = models.CharField(max_length=6, default=default_pin_code)
    created_at = models.DateTimeField(default=default_date)
    use_before = models.DateTimeField(default=default_date_plus_five_min)
    used = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pin_code
