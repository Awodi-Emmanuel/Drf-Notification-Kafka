from notif.emailer import Emailer
from notif.smsers import ExternalSMS
from notif.pusher  import Pusher
import logging
import traceback

logger = logging.getLogger()

def nofify(
    vias: list,
    subject: str = None,
    receivers: list = None,
    template: str = None,
    context: dict = {},
    smtp_account: str = None,
    threaded: bool = False,
):
    logger.info(f"Sending {subject} to {receivers} via {vias}")
    for via in vias:
        try:
            if via == "email":
                em = Emailer(
                    subject,
                    receivers,
                    template,
                    context,
                    smtp_account,
                    threaded=threaded
                )
                em.send()
            
            elif via == "external_sms":
                ex_sms = ExternalSMS(receivers, template, context, threaded=threaded)
                ex_sms.send()
            
            elif via == "push":
                pusher = Pusher(
                    subject, receivers, template, context, threaded=threaded
                )
                pusher.send()
            
            else:
                logger.error(f"Unkown sending method {via}")
        except:
            logger.error(traceback.format_exc())
              