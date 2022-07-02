from ensurepip import bootstrap
import enum 
from kafka import kafkaConsumer
import json
import consumer.proccessor as proccess

BOOTSTRAP_SERVERS = ['localhost:9092']

class ActionType(enum.Enum):
    notification = "notification"
    default = "notification"
    
    
def register_kafka_listener(topic, listener):
    # poll kafka 
    def poll():
        # Initialize consumer instance
        consumer = kafkaConsumer(topic, bootstrap_servers=BOOTSTRAP_SERVERS)
        for msg in consumer:
            # print("Enter the loop/nkey: ", msg.key, "Value:", msg.value)
            kafka_listener(msg)
    poll()
    
def kafka_listener(data):
    log: bool = proccess.log_notification(json.loads(data.value.decode("utf-8")))
    
    if log == True:
        proccess.send_notification(json.loads(data.value.decode("utf-8")))
        print(json.loads(data.value.decode("utf-8"))['req_id'])
        
    else:
        #TODO: Notify system of Logger error
        print("unable to log and notify user")   
           
register_kafka_listener(ActionType.notification.value, kafka_listener)           