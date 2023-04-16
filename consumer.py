# Based on from https://www.youtube.com/watch?v=VHngQ-moXIE
""" 
Simple kafka consumer
"""
# import time
import os

from dotenv import load_dotenv

load_dotenv()

from kafka import KafkaConsumer
from kafka.coordinator.assignors.roundrobin import RoundRobinPartitionAssignor

# Set up the consumer group and topic to consume from
consumer_group = "my_consumer_group"
topic = "my_topic"

# Set up the Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=os.environ["ULR_BROKER"],
    group_id=consumer_group,
    auto_offset_reset="earliest",
    partition_assignment_strategy=[RoundRobinPartitionAssignor],
)


# TOPIC_NAME = "items"

# consumer = KafkaConsumer(
#     TOPIC_NAME, bootstrap_servers=["localhost:9092"]
# )

for message in consumer:
    print(message)
