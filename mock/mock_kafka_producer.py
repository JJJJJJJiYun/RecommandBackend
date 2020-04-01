import json
import random
import time

from kafka import KafkaProducer

while True:
    msg = {
        'user_id': random.randint(1, 100),
        'item_id': random.randint(1, 200),
        'score': random.randint(1, 10),
        'action': 'read'
    }
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             bootstrap_servers=['127.0.0.1:9092'])
    producer.send('user_action', msg)
    time.sleep(2)
