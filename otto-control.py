import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

pins = {
	24 : {'name': 'motor', 'state': GPIO.LOW},
	25 : {'name': 'motor', 'state': GPIO.LOW}
}

# Set each pin as an output and make it LOW

for pin in pins: 
	GPIO.setup(pin, GPIO.OUT)