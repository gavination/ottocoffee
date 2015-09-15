import RPi.GPIO as GPIO
from flask import Flask, render_template, request
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
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'HELLO!',
        'time': timeString
        }
    pwm.start(0)
    return render_template('main.html', **templateData)

@app.route("/forward")
def forward():
    templateData = {
        'value': '50',
        'title': 'FORWARD'
    }
    pwm.start(50)
    return render_template('dir.html')
    
@app.route("/backward")
def backward():
    templateData = {
        'value': '2',
        'title': 'BACKWARD'
    }
    pwm.start(2)
    return render_template('dir.html')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)