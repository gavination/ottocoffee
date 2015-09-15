import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import datetime
app = Flask(__name__)

from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
#pwm.start(5)





# root = Tk()
# root.wm_title('Servo Control')
# app = App(root)
# root.geometry("200x50+0+0")
# root.mainloop()


@app.route("/")
def main():
    pwm.start(0)
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time': timeString
        }
    
    return render_template('main.html', **templateData)

@app.route("/forward")
def forward():
    pwm.start(50)
    templateData = {
        'value': '50',
        'title': 'FORWARD'
    }
    return render_template('dir.html')
    
@app.route("/backward")
def backward():
    pwm.start(2)
    templateData = {
        'value': '2',
        'title': 'BACKWARD'
    }
    return render_template('dir.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)