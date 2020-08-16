#!/bin/bash

echo 'Consumer Messages Received:'
wc -l /logs/consumer_*
echo 'Producer Messages Sent:'
wc -l /logs/producer_*