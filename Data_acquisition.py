from pyArduino import * 
from tkinter import *
import datetime
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import threading

isRun = True
isReceive = False
TempMin = 100
TempMax = 0

tiempo = datetime.datetime.now() #Tiempo in spanish means time

ts = 1
tf = 30
t = np.arange(0,tf+ts,ts)
N = len(t)

tempMin = 0

port = 'COM3' #This port is according to where arduino was connected
baudRate = 9600
sizeData = 1

if isRun:
    arduino = serialArduino(port,baudRate,sizeData)
    arduino.readSerialStart()
    print(f"   Day           Hour        Temperature")

y = np.zeros((sizeData,N))

def getValue():
    global isRun
    global samples
    time.sleep(0.5)
    while isRun:

        for k in range(N):

             start_time = time.time()

        for n in range(sizeData):
    
            y[0,k] = arduino.rawData[0]

            print(tiempo.strftime('%d/%m/%Y     %H:%M:%S'), f"       {y[0,k]}")

        elapsed_time = time.time() - start_time

        while elapsed_time<ts:
            elapsed_time = time.time()-start_time

hilo1 = threading.Thread(target=getValue,
                         daemon=True) #Create a thread before serial communication starts

def Start():  
    global isReceive
    isReceive = True
    hilo1.start()

def Stop():    
    global isRun
    global y
    isRun=False
    arduino.close() #Close serial communication
    hilo1.join(0.1)
    
def Min():
    global TempMin
    value = arduino.rawData[0]
    if value < TempMin:
        TempMin = value
        lblMin["text"] = TempMin

def Max():
    global TempMax
    value = arduino.rawData[0]
    if value > TempMax:
        TempMax = value
        lblMax["text"] = TempMax
            
ventana = Tk()
ventana.title("Lectura temperatura")
ventana.geometry("400x200") #Window size
ventana["bg"]="gray77"

btnStart = Button(ventana, text="Start", command = Start)
btnStart["fg"]="black"
btnStart["bg"]="lime green"
btnStart["font"]="Helvetica 12"
btnStart.place(x=30,y=30,width=100,height=60)

btnStop = Button(ventana, text= "Stop", command = Stop)
btnStop["fg"]="black"
btnStop["bg"]="orange red"
btnStop["font"]="Helvetica 12"
btnStop.place(x=150,y=30,width=100,height=60)

btnMinimo = Button(ventana, text= "Temperatura Minima", command = Min)
btnMinimo["fg"]="black"
btnMinimo["bg"]="SkyBlue3"
btnMinimo.place(x=30,y=110,width=150,height=30)

btnMaxima = Button(ventana, text= "Temperatura Maxima", command = Max)
btnMaxima["fg"]="black"
btnMaxima["bg"]="gold"
btnMaxima.place(x=30,y=160,width=150,height=30)

lblMin= Label(ventana)
lblMin["fg"]="black"
lblMin["bg"]="SkyBlue3"
lblMin.place(x=200,y= 110, width=150,height=30)

lblMax= Label(ventana)
lblMax["fg"]="black"
lblMax["bg"]="gold"
lblMax.place(x=200,y= 160, width=150,height=30)

ventana.mainloop()
