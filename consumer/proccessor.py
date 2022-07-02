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
    
def log_notification(data: dict) -> bool:
    
    request_id = data['req_id']
    stream_id = data["stream_id"]
    message = data['message']
    destination = data['message']['email'] if data['channel'] == 'email' else data['message']['phone']
    source_service = data['source']
    notification_type = data['notification_type']
    channel = data['channel']
    
    try:
        NotificationsRequest.objects.create(
            request_id=request_id,
            stream_id=stream_id,
            message=message,
            destination=destination,
            source_service=source_service,
            notification_type=notification_type,
            channel=channel
            
        ) 
        return True   
    except Exception as e:
        return False