from ast import Try
from notif import notifier
from notif.models import NotificationsRequest

def send_notification(data: dict):
    
    {
        "req_id": "halkjhdflkjfdlkjhg",
        "stream_id": "hkajdfhjgkhgjhk",
        "message": {
            "subject": "Restet Password",
            "email": "traze@gmail.com",
            "reset_url": "https://sellanithing.com/reset/?token=MTIzNDU=&email=dHJhemVAZ21haWwuY29t",
            "username": "Awodi"
        },
        "notification_type": "reset_init",
        "channel": "sms"
        
    }
    
    vias = data["channel"]
    subject = data['message']['subject']
    receiver = data['message']['email'] if vias == 'email' else data['message']['phone']
    notification_type = data['notification_type']
    context = data['message']
    
    notifier.notify(vias=[vias],
                    subject=subject,
                    receivers=[receiver],
                    template=notification_type,
                    context=context,
                    smtp_account="account",
                    thread=True
                    )
    
    