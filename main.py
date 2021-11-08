#!/usr/bin/python3
import os
import sys
from telnetlib import Telnet
from multiprocessing import Process
import time
import csv
import pandas
from pandas.core import frame


DMM = ["169.254.1.2", "169.254.1.3"]

DMM0data=''
DMM1data=''


def connect_telnet(host, port):
    with Telnet(host, port) as tn:
        tn.write(b"SYST:REM\r\n")
        #tn.write(b"*IDN?\r\n")
        #time.sleep(0.1)
        #print(tn.read_eager().decode('ascii'))
        time.sleep(0.1)
        if host==DMM[0]:
            tn.write(b"MEAS:VOLT:DC? 10\r\n")
        elif host==DMM[1]:
            tn.write(b"MEAS:CURR:DC? 10\r\n")
        else:
            print("Error. Retry")
        time.sleep(0.3) # at least 0.25
        # print(tn.read_eager().decode('ascii')) # this one used originally
        #print(tn.read_all().decode('ascii'))
        # save printed data to variable
        if host==DMM[0]:
            global DMM0data 
            DMM0data= tn.read_eager().decode('ascii').replace('\r\n', '')
        elif host==DMM[1]:
            global DMM1data
            DMM1data = tn.read_eager().decode('ascii').replace('\r\n', '')
        else:
            print('Invalid host argument')


        



# change argument to cell number "O" "L"
def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("No arguments provided.")
        exit(1)
    print("connecting for Cell # ", args[0])
    cell_num = int(args[0])
    if cell_num < 0:
        print("Invalid Cell number.")
        exit(1)
    connect_telnet(DMM[0], 3490)
    connect_telnet(DMM[1], 3490)
    
    if args[1] == 'O':
        frame = {
                'Cell #' : [int(args[0])],
                'Voc'   : [DMM0data],
            }
        df = pandas.DataFrame(frame) 
        df.to_csv('Voc.csv', mode='a', index=False, header=False)
    elif args[1] == 'L':
        frame = {
                'Cell #' : [int(args[0])],
                'V_load'   : [DMM0data],
                'I_load'   : [DMM1data]
            }
        df = pandas.DataFrame(frame) 
        df.to_csv('loaded.csv', mode='a', index=False, header=False)

    # row_data = [args[0], DMM0data, DMM1data]
    # with open('internalResistance.csv','w',  newline='') as csvfile:
    #     my_writer = csv.writer(csvfile, delimiter = ' ')
    #     my_writer.writerow(row_data)


if __name__ == "__main__":
    main()
