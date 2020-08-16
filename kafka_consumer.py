#!/usr/bin/python3
import sys
import yaml
import msgpack
from datetime import datetime
from kafka import KafkaConsumer

group_id = 'consumer_group_' + sys.argv[1]

# Load Config
config = yaml.load(open('./kafka_consumer.yaml'), Loader=yaml.FullLoader)

# Initialize Consumer
consumer = KafkaConsumer(
    group_id=group_id,
    value_deserializer=msgpack.unpackb,
    bootstrap_servers=config['bootstrap_servers']
)

# Subscribe to all topics
topics = consumer.topics()
print ("Total Topics Found: {}".format(len(topics)))
consumer.subscribe(list(topics))

for message in consumer:
    print("[{}]: RECEIVE: {}:{}:{}: key={} value={}".format(
        datetime.now().isoformat(),
        message.topic,
        message.partition,
        message.offset,
        message.key,
        message.value
    ))
