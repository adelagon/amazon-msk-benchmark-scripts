#!/usr/bin/python3
import sys
import time
import yaml
import random
import msgpack
from datetime import datetime
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer_id = 'producer_' + sys.argv[1]

# Load Config
config = yaml.load(open('./kafka_producer.yaml'), Loader=yaml.FullLoader)

# Initialize Producer
producer = KafkaProducer(
    value_serializer=msgpack.dumps,
    bootstrap_servers=config['bootstrap_servers']
)

def on_send_success(record_metadata):
    pass

def on_send_error(e):
    print("ERROR: {}".format(e))

### Create Topics
i = 1
while 1:
    topic = config['topic_prefix'] + str(random.randrange(1, config['num_topics']))
    message = "Message from: " + producer_id + " Count: " + str(i)
    print("[{}]: SEND: {}".format(datetime.now().isoformat(), message))
    producer.send(topic, {'key': message}).add_callback(on_send_success).add_errback(on_send_error)
    i += 1

producer.flush()