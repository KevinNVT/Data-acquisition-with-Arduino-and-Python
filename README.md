# Data-acquisition-with-Arduino-and-Python

![MadeWPython](http://ForTheBadge.com/images/badges/made-with-python.svg)
![MadeWPython](http://ForTheBadge.com/images/badges/built-with-love.svg)
<br />
![GitHub last commit](https://img.shields.io/github/last-commit/KevinNVT/Data-acquisition-with-Arduino-and-Python)
![Follow](https://img.shields.io/github/followers/KevinNVT.svg?style=social&label=Follow&maxAge=2592000)

>Data acquisition with Arduino and Python registered in Excel.
><br />
[PyArduino](https://roboticoss.com/modulo-pyarduino-lectura-de-datos/) for data acquisition used.
>

### Features

✅ Data acquisition with Arduino using library pyArduino. <br />
✅ Real-time graph of the data. <br />
✅ Data entry in Excel. <br />
✅ GUI using [tkinter](https://docs.python.org/3/library/tkinter.html). <br />
✅ Display for maximum and minimum value. <br />

### Install librarys
```markdown
python –m pip install tk
```

Download [PyArduino](https://roboticoss.com/modulo-pyarduino-lectura-de-datos/) for data acquisition with Arduino. 

### Get data from Arduino 

```python
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
```

```python
arduino = serialArduino(port,baudRate,sizeData)
    arduino.readSerialStart()
    print(f"   Day           Hour        Temperature")
```

### Get temperature min

```python
def Min():
    global TempMin
    value = arduino.rawData[0]
    if value < TempMin:
        TempMin = value
        lblMin["text"] = TempMin
```

### Get temperature max

```python
def Max():
    global TempMax
    value = arduino.rawData[0]
    if value > TempMax:
        TempMax = value
        lblMax["text"] = TempMax
```

### GUI

Graphic User Interface showing buttons for start and stop, temperature, date, hour, temperature min and max. 



<img align="left" src="https://github.com/KevinNVT/Data-acquisition-with-Arduino-and-Python/blob/main/img/GUI.jpg" width="350px">
<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />


### Real - time graph

Graph. 

<img align="left" src="https://github.com/KevinNVT/Data-acquisition-with-Arduino-and-Python/blob/main/img/Graph.jpg" width="350px">
<br />
