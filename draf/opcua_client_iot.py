import paho.mqtt.client as mqtt
from random import randint
import time
import json
import string
import random



iot_hub = "demo.thingsboard.io"
port = 1883
username = "aETE3LfY1hNKwzF2n7Zv"  # Paste your access token here
password = ""
topic = "v1/devices/me/telemetry"

iot_hub_client = mqtt.Client()
iot_hub_client.username_pw_set(username, password)
iot_hub_client.connect(iot_hub, port)
print("Connected to IOT hub")

data = dict()
while True:
    try:
        temperature = "Chai"
        pressure = "Hello"



        def get_random_string(length):
        # choose from all lowercase letter
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))
            #print("Random string of length", length, "is:", result_str)
        temperature = get_random_string(5)
        pressure = get_random_string(4)
        print(temperature, pressure)
        data["temperature"] = str(temperature)
        data["pressure"] = str(pressure)
        data_out = json.dumps(data)
        iot_hub_client.publish(topic, data_out, 0)

        time.sleep(2)
    except Exception as e:
        print(e)
