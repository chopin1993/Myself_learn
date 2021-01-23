# coding:utf-8
import time
import serial

ser = serial.Serial("COM3", 9600, timeout=5)
ser.flushInput()


def main():
    while True:
        back = ser.inWaiting()
        if back != 0:
            recv = ser.read(ser.in_waiting).decode("gbk")
            print(time.time(), "--recv--", recv)
        time.sleep(0.1)


if __name__ == "__mian__":
    main()
