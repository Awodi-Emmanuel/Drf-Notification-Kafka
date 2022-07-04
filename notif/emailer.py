from django.core.mail import get_connection, send_email 
from django.core.mail.message import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from threading import Thread
from django.conf import settings
import traceback
import re
import unidecode 
import logging 
from django.utils.translation import gettext as _ 
from django.utils.translation import activate

logger = logging.getLogger("smtp")

class Emailer:
    def __init__(
        self,
        subject: str,
        receivers: list,
        template: str,
        context: dict,
        smtp_account: str,
        **kwargs,
    ):
        smtp_host = settings.SMTP.get("host")
        smtp_port = settings.SMTP.get("port")
        smtp_use_tls = settings.SMTP.get("use_tls")
        smtp_use_ssl = settings.SMTP.get("use_ssl")
        smtp_username = settings.SMTP.get("accounts").get(smtp_account).get("username")
        smtp_password = settings.SMTP.get("accounts").get(smtp_account).get("password")
        self.smtp_from = settings.SMTP.get("accounts").get(smtp_account).get("from")
        
        self.connection = get_connection(
            host=smtp_host,
            port=smtp_port,
            username=smtp_username,
            password=smtp_password,
            use_tls=smtp_use_tls,
            use_ssl=smtp_use_ssl
        )
        
        
    def send(self):