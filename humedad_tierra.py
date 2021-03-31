import RPi.GPIO as GPIO
import time

class Tempt():
    
    GPIO.setmode(GPIO.BCM)
     
    channel = 17

    GPIO.setup(channel, GPIO.IN)

    def MedirHumedad():
        valor = GPIO.input(17)
        print("valor ", valor)
        if valor == 0:
            print("humedo")
        else:
            print("seco")
    while True:
        MedirHumedad()
        time.sleep(2)