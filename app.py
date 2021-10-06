from machine import Pin
from umqtt.simple import MQTTclient
import time 
import webrepl

B1=Pin(5, Pin.IN)
B2=Pin(14,Pin.IN)

cliente = MQTTclient('andres' , 'maqiatto.com' , 1883, 'andresandino36@gmail.com' , 'Andres623Eloy')

def conectado(tcp,msg):
	x=len(msg)
	print(str(x))
	y=len("ON")
	z=len("OFF")

	if x==y:
		cliente.publish("andresandino36@gmail.com/T2",str(a))
    else:
    	 if x==z:
			cliente.publish("andresandino36@gmail.com/T2" , "S1:" +str(st))

cliente.set_callback(conectado)
cliente.connect()
cliente.subscribe("andresandino36@gmail.com/T1")

rc=0
while rc==0:
	boton1=B1.value()
	if (boton1==0):
		a=1
		h=open("prue1.txt" , 'a')
		h.write("S1:" +str(a)+";" + "S2:" +str(b)+";" + "\n" )
		h.close()
		h=open("prue1.txt" , 'r+')
		tr=h.read()
		time.sleep(3)
		print ("sensor 1:" , +str(tr))
		h.close()
		time.sleep(0.3)
	else:
		a=0

	boton2=B2.value()
	if(boton2==0):
		b=1
		d=open("nombre.txt" , 'a')
		d.write("S1:" +str(a)+ ";" + "S2:" +str(b) + ";" + "\n")
		d.close()
		d=open("nombre.txt" , '+r')
		tr=d.read()
		time.sleep(4)
		print("S1:" +str(tr))
		d.close()
		time.sleep(0.3)
	else:
		b=0

	cliente.check_msg()
