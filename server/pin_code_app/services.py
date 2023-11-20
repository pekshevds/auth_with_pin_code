from django.utils import timezone
from django.db.models.query import QuerySet
from pin_code_app.models import Record
from auth_app.models import CustomUser


def not_used_users_records(user: CustomUser):
    return Record.objects.filter(
        user=user,
        use_before__gte=timezone.now(),
        used=False
    )


def not_used_users_record_by_pin_code(
        records: QuerySet,
        pin_code: str) -> [Record, None]:

    for record in records:
        if record.pin_code == pin_code:
            return record
    return None


def add_record(user: CustomUser):
    record = Record(user=user)
    record.save()


def use_record(record: Record):
    record.used = True
    record.save()
