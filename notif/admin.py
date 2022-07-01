from django.contrib import admin
from notif.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass

