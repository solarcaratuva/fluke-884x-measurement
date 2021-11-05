#!/usr/bin/python3
import os
import sys
from telnetlib import Telnet
from multiprocessing import Process
import time

DMM = ["169.254.1.2", "169.254.1.3"]


def connect_telnet(host, port):
    with Telnet(host, port) as tn:
        tn.write(b"SYST:REM\r\n")
        #tn.write(b"*IDN?\r\n")
        #time.sleep(0.1)
        #print(tn.read_eager().decode('ascii'))
        time.sleep(0.1)
        tn.write(b"MEAS:VOLT:DC? 10\r\n")
        time.sleep(0.25)
        print(tn.read_eager().decode('ascii'))
        #print(tn.read_all().decode('ascii'))


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("No arguments provided.")
        exit(1)
    print("connecting DMM", args[0])
    dmm_index = int(args[0])
    if dmm_index > len(DMM) or dmm_index < 0:
        print("Invalid DMM index.")
        exit(1)
    connect_telnet(DMM[dmm_index], 3490)


if __name__ == "__main__":
    main()
