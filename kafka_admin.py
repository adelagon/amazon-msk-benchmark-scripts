#!/usr/bin/python3
import yaml
from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError

# Load Config
config = yaml.load(open('./kafka_admin.yaml'), Loader=yaml.FullLoader)

# Initialize Consumer
consumer = KafkaConsumer(
    bootstrap_servers=config['bootstrap_servers']
)
# Initialize Admin
admin = KafkaAdminClient(
    bootstrap_servers=config['bootstrap_servers']
)

# Clean up topics
topics = consumer.topics()
print("Found {} topics".format(str(len(topics))))
if config['clean_topics_on_start']:
    for topic in topics:
        print("Deleting Topic: {}".format(topic))
        admin.delete_topics([topic])

# Create topics
print("Creating {} topics...".format(config['num_topics']))
for i in range(1, config['num_topics']+1):
    topic_name = config['topic_prefix'] + str(i)
    print("Creating Topic: {}".format(topic_name))
    admin.create_topics([NewTopic(
        name=topic_name,
        num_partitions=config['num_partitions'],
        replication_factor=config['replication_factor']
    )])

print("Done!")