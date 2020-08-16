#!/usr/bin/python3
import re
import sys
from datetime import datetime, timedelta
from statistics import mean

consumer_logs = sys.argv[1]
producer_logs = sys.argv[2]


print ("Parsing Consumer Logs: {} Please wait.".format(consumer_logs))
consumer_ts = {}
with open(consumer_logs, 'r') as cl:
    for line in cl:
        ts = re.search(r'\[(.*?)\]', line)
        count = re.search(r'Count: (.*?)\'', line)
        if ts:
            consumer_ts[count.group(1)] = datetime.fromisoformat(ts.group(1))

print ("Parsing Producer Logs: {} Please wait.".format(producer_logs))
producer_ts = {}
with open(producer_logs, 'r') as pl:
    for line in pl:
        ts = re.search(r'\[(.*?)\]', line)
        count = re.search(r'Count: (.*?)\'', line)
        if ts:
            producer_ts[count.group(1)] = datetime.fromisoformat(ts.group(1))

print("Calculating Deltas...")
deltas = []
for num, consumer_ts in consumer_ts.items():
    try:
        delta = consumer_ts - producer_ts[num]
        deltas.append(delta.total_seconds())
    except:
        pass

print("Calculating Average...")
print("Messages Processed: {}".format(len(deltas)))
print("Average Latency: {}".format(mean(deltas)))