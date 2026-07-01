import serial
ser = serial.Serial('COM4', 500000)
with open("output.pcm", "wb") as f:
    while True:
        f.write(ser.read(1024))
        
        
