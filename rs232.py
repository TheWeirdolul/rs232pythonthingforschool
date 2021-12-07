import serial
from serial.serialutil import EIGHTBITS, STOPBITS_ONE

ser = serial.Serial (
    port='dev/tty/0',
    baudrate=19200,
    databits = EIGHTBITS,
    stopbits = STOPBITS_ONE,
    oddevencheck = None
)


ser.open()
ser.write(hex("7F 08 99 A2 B3 C4 02 FF 01 00 CF"))
ser.read()
print(ser.read)
ser.close()