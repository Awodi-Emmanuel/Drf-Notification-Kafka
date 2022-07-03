import json 
from channels.generic.websockect import WebsocketConsumer
import logging
import traceback 
from ctypes
from pathlib import Path
import binascii
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from datetime import date, datetime, timedelta
from notif.models import Notification
from notif.models_serializers import NotificationSerializer
from django.utils import timezone

logger = logging.getLogger("notif")

class PushNotifConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token: str = None
        self.user = None
        
    def connect(self):
        try:
            self.accept()
            
            self.token = self.scope["url_route"]["kwargs"]["token"]
            db_tok = Token.objects.get(key=self.token)
            self.user = db_tok.user
            
            self.user.settings.push_channel = self.channel_name
            self.user.settings.save()
            
            logger.info("Accepted")
        except Exception as e:
            print(traceback.print_exc())
            logging.error(traceback.format_exc()) 
            
    def disconnect(self, close_code):
        try:
            self.user.settings.push_channel = None
            self.user.settings.save()
        except Exception as e:
            print(traceback.format_exc())
            logging.error(traceback.format_exc())