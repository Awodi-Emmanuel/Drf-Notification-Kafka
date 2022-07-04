from django.dispatch import receiver
from notif.cgsms_client import CGSmsClient
from threading import Thread
from django.template.loader import render_to_string
import logging
import traceback

logger = logging.getLogger("notif")

class ExternalSMS:
    def __init__(self, receivers: list, template: str, context: dict, **kwargs):
        self.receivers: list = receivers
        self.template: str = template
        self.context: dict = context
        self.threaded: bool = kwargs.get("threaded", False)
        
    def send(self):
        if self.threaded:
            t = Thread(target=self._send)
            t.setDaemon(True)
            t.start()
        else:
            self._send()
            
    def _send(self):
        try:
            for rec in self.receivers:
                ctx = self.context.copy()
                ctx["user"] = rec
                sms_content = render_to_string("{}/sms.text".format(self.template), ctx)
                
                CGSmsClient.send(rec.number, sms_content)
        except:
            logger.error(traceback.format_exc())
            

if __name__ == "__main__":
    pass