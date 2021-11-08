# fluke-884x-measurement
Use Fluke 8845A DMM over telnet to measure battery cells

Running it: 
    Do "Run Python File in Terminal", just to get the line below
        & "C:/Program Files/Python/Python310/python.exe" "c:/Users/daich/Desktop/Solar Car/GitHub stuff/Fluke/fluke-884x-measurement/main.py" 
    Path will depend on where you have it saved. 
    Add 2 arguments: integer for the cell number, and either "O" for open or "L" for loaded.  

Setting up DMMs
On multimeter LAN, 8845 command
E825383
DHCP=Off
IP=169.254.001.002
NETMASK=255.255.254.0

E825394
DHCP=Off
IP=169.254.001.003
NETMASK=255.255.254.0

Host computer
Link-local static address: 169.254.1.1/23

Telnet command
telnet 169.254.1.x 3490

*IDN? // print identifier
SYST:REM // puts meter in remote mode
MEAS:VOLT:DC? 10 // measure DC Voltage range 10V
 