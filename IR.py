import RPi.GPIO as GPIO
import requests
import time

# ThingSpeak parameters
WRITE_API_KEY = "YOUR_THINGSPEAK_WRITE_API_KEY"
CHANNEL_ID = "YOUR_CHANNEL_ID"

# IR sensor pin
IR_PIN = 18

# Configure GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)

def send_to_thingspeak(data):
    url = f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}&field1={data}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Data sent to ThingSpeak successfully")
        else:
            print(f"Failed to send data to ThingSpeak. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception occurred while sending data to ThingSpeak: {e}")

try:
    while True:
        ir_status = GPIO.input(IR_PIN)
        if ir_status:
            print("IR detected")
            send_to_thingspeak(1)
        else:
            print("No IR detected")
            send_to_thingspeak(0)
        time.sleep(15)  # Adjust the delay according to your requirement
except KeyboardInterrupt:
    GPIO.cleanup()
