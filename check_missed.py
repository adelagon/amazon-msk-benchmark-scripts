#!/usr/bin/python3
import re

last_message = 0
with open('logs/consumer.log', 'r') as f:
    for line in f:
        count = re.search(r'Count: (.*?)\'', line)
        if count:
            if last_message != int(count.group(1))-1:
                print ("Missing Message: {}".format(count.group(1)))
            else:
                last_message = int(count.group(1))