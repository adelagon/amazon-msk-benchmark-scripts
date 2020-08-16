#!/bin/bash

echo 'Starting consumers...'
for c in {1..15}
do
    nohup ./kafka_consumer.py $c > /logs/consumer_$c.log &
    sleep .5
done

echo 'Starting producers...'
for p in {1..200}
do
    nohup ./kafka_producer_confluent.py $p > /logs/producer_$p.log &
    sleep .5
done

echo 'Now sit back and watch the bees...'