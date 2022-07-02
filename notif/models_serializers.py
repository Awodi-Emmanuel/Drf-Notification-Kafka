from rest_framework.serializers import ModelSerializer
from notif.models import Notification

class NotificationSerializer(ModelSerializer):
    models = Notification
    feilds = (
        "text",
        "type",
        "sub_type",
        "link",
        "image",
        "actions",
        "data",
        "read",
        "sent",
        "mode"
        
         
    )