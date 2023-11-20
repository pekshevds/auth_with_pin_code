from django.contrib import admin
from pin_app.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        '__str__', 'pin_code', 'created_at',
        'use_before', 'used', 'user',)
    list_filter = ('user',)
