from django.contrib import admin
from .models import AdvUser

# Register your models here.

@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('is_activated', 'send_messages',)
