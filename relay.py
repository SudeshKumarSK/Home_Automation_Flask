from flask import *
import time
import RPi.GPIO as GPIO
# from flask-ngrok import run_with_ngrok 



GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers 

f = 26      # Fan pin
t1 = 19     # Fan pin
t2 = 6      # Fan pin
b = 13      # Fan pin
ac = 5      # Fan pin

#Making the pins as OUTPUT pins
GPIO.setup(f, GPIO.OUT) # GPIO Assign mode
GPIO.setup(t1, GPIO.OUT)
GPIO.setup(t2, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(ac, GPIO.OUT)

app = Flask(__name__)

# run_with_ngrok(app)  # Start ngrok when app is run



@app.route('/room')
def index():
    return render_template('room.html')  #Render the HTML page


@app.route('/signup', methods = ['Post'])
def signup():
    fan = request.form['fan']
    #print("Fan relay value is :"+fan )


    
    if fan == "f1":
       GPIO.output(f, GPIO.LOW)  #Switch ON fan
       
    elif fan == "f0":
         GPIO.output(f, GPIO.HIGH) #Switch OFF fan



    elif fan == "t11":
         GPIO.output(t1, GPIO.LOW) #Switch ON Tubelight1

    elif fan == "t10":
         GPIO.output(t1, GPIO.HIGH) #Switch OFF Tubelight1



    elif fan == "t21":
         GPIO.output(t2, GPIO.LOW) #Switch ON Tubelight2
    elif fan == "t20":
         GPIO.output(t2, GPIO.HIGH) #Switch OFF Tubelight2



    elif fan == "b1":
         GPIO.output(b, GPIO.LOW) #Switch ON Balconylight

    elif fan == "b0":
         GPIO.output(b, GPIO.HIGH) #Switch OFF Balconylight


    elif fan == "ac1":
         GPIO.output(ac, GPIO.LOW) #Switch ON AC

    elif fan == "ac0":
         GPIO.output(ac, GPIO.HIGH) #Switch OFF AC
    #GPIO.cleanup(17)    
    return  render_template('room.html')
if __name__ == '__main__':
    app.run(threaded=True)

