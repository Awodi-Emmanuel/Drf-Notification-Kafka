from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _ 
from django.db.models import JSONField

User = get_user_model()

class Notification(models.Model):
    MODE_CLIENT = "client"
    MODE_SHOP = "shop"
    MODE_ADMIN = "admin"
    MODES = [
        (MODE_CLIENT, MODE_CLIENT),
        (MODE_SHOP, MODE_SHOP),
        (MODE_ADMIN, MODE_ADMIN),
    ]

    user: models.ForeignKey = models.ForeignKey(
        User, models.CASCADE, related_name="notifications"
    )
    text: models.TextField = models.TextField()
    type: models.CharField = models.CharField(max_length=30)
    sub_type: models.CharField = models.CharField(max_length=30, null=True, blank=True)
    link: models.CharField = models.CharField(_("The link associated"), max_length=255)
    image: models.ImageField = models.ImageField(upload_to="notifications")
    actions: JSONField = JSONField(default=dict)
    data: JSONField = JSONField(default=dict)
    read: models.DateTimeField = models.DateTimeField(null=True, blank=True)
    sent: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    mode: models.CharField = models.CharField(
        max_length=10, default=MODE_CLIENT, choices=MODES
    )

    def __str__(self):
        if self.user and self.user.name:
            user_name = self.user.name
        else:
            user_name = ""
        return "{} Notif #{}".format(user_name, self.id)
        
        
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs) 
    
    
class NotificationsRequest(models.Model):
    {
        "req_id": "halkjhdflkjfdlkjhg",
        "stream_id": "hkajdfhjgkhgjhk",
        "message": {
            "subject": "Reset Password",
            "email": "traze@gmail.com",
            "reset_url": "https://sellanithing.com/reset/?token=MTIzNDU=&email=dHJhemVAZ21haWwuY29t",
            "username": "Awodi"
            
        },
        "notification_type": "reset_init",
        "channel": "sms"
    }              
    
    request_id: models.CharField = models.CharField(max_length=50, null=False, blank=False)
    stream_id: models.CharField = models.CharField(max_length=50, null=False, blank=False)
    message: JSONField = JSONField(default=dict)
    destination: models.CharField = models.CharField(max_length=200, null=False, blank=False)
    source_service: models.CharField = models.CharField(max_length=50, null=False, blank=False)
    notification_type: models.CharField = models.CharField(max_length=50, null=False, blank=False)
    channel: models.CharField = models.CharField(max_length=50, null=False, blank=False)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateField = models.DateField(auto_now=True)
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)