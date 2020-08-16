#!/usr/bin/python3
import sys
import yaml
import random
import msgpack
from datetime import datetime
from confluent_kafka import Producer

producer_id = 'producer_' + sys.argv[1]

# Load Config
config = yaml.load(open('./kafka_producer.yaml'), Loader=yaml.FullLoader)
bootstrap_servers = ",".join(config['bootstrap_servers'])

# Initialize Producer
producer = Producer({
    'bootstrap.servers': bootstrap_servers
})

def on_delivery(e, msg):
    if e:
        print('ERROR: {}'.format(e))
    else:
        print("[{}]: SEND: {}: {}".format(datetime.now().isoformat(), msg.topic(), msgpack.unpackb(msg.value())))

i = 1

while 1:
    producer.poll(0)
    topic = config['topic_prefix'] + str(sys.argv[1])
    message = "Message from: " + producer_id + " Count: " + str(i)
    producer.produce(topic, value=msgpack.dumps({'key': message}), callback=on_delivery)
    if i % config['flush_until'] == 0:
        producer.flush()
    i += 1

producer.poll(0)