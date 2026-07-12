Just my first VSCode project setup using Joseph Fergusson's micro:bit extension for VSCode.

It gets the library stubs, and can flash to device.

To see extension output: output tab, then select microdot from the right.

Flashing: initially wasn't working. Output showed can't find 'ufs' command so I made a .bat file for it. It does try alternatives but only the .bat worked. Had to do same for uflash. 

Buildto copies MicroPython .hex file first, then reboots and drops main.py script to run. 
Put-this-file just copies the .py file to the code area (separate to USB disk area). 
One reboot main.py script is run by uPython hex system. 

USB serial post debugging works when you select USB com port. I think that blocks the flashing too...

