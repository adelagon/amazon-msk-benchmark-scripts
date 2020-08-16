#!/usr/bin/python3
import sys
import yaml
import msgpack
from datetime import datetime
from confluent_kafka import Consumer

group_id = 'consumer_group_' + sys.argv[1]

# Load Config
config = yaml.load(open('./kafka_consumer.yaml'), Loader=yaml.FullLoader)
bootstrap_servers = ",".join(config['bootstrap_servers'])

# Initialize Consumer
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'end'
})

# Subscribe to all topics
topics = list(consumer.list_topics().topics.keys())
print ("Total Topics Found: {}".format(len(topics)))
consumer.subscribe(topics)

count = 0
while 1:
    message = consumer.poll(1.0)

    if message is None:
        continue
    if message.error():
        print ('ERROR: {}'.format(message.error()))
    
    print("[{}]: RECEIVE: {}:{}:{}: key={} value={}".format(
        datetime.now().isoformat(),
        message.topic(),
        message.partition(),
        message.offset(),
        message.key(),
        msgpack.unpackb(message.value())
    ))

    if count % config['min_commit_count'] == 0:
        consumer.commit()
        
consumer.close()