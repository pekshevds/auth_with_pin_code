from django.contrib import admin
from auth_app.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'last_login',)
