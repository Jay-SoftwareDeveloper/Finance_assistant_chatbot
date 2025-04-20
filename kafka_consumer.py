from kafka import KafkaConsumer
import json
from azure_sql import insert_expense

consumer = KafkaConsumer(
    'expenses',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("[Consumer] Listening...")
for message in consumer:
    data = message.value
    insert_expense(data)