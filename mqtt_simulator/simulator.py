import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("mqtt_broker", 1883, 60)  # ganti jika broker bukan 'mqtt_broker'

while True:
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 50.0)
    payload = f'{{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}}'
    client.publish("sensor/data", payload)
    print("Published:", payload)
    time.sleep(5)
