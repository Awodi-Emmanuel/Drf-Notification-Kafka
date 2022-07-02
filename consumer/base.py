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
    
                    