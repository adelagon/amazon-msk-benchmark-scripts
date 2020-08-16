# Amazon MSK Benchmark Scripts:

## Abstract
The following scripts can be used for benchmarking Amazon MSK or any Kafka installations. These can be used for the following tests:
* **Throughput** - messages per second
* **Latency** - end-to-end delivery
* **Resiliency** - delivery completeness during broker failure
  
## Main scripts
* **kafka_admin.py** - creates topics
* **kafka_producer.py** - kafka producer (kafka-python), legacy and a bit slow *do not use*
* **kafka_producer_confluent.py** - kafka producer using `confluent-kafka`
* **kafka_consumer.py** - kafka consumer
* ***.yaml** - configuration files, update as needed.
  
## Helper scripts
* **attack.sh** - instantiates producers and consumers. Use for throughput tests.
* **restart.sh** - kills all running python apps and cleans up logs.
* **count_logs.sh** - counts all messages produced and consumed from logs.
* **calculate_latency.py** - checks the actual end-to-end message delivery from logs.
* **check_missed.py** - checks if the messages received are complete and in order from logs.
