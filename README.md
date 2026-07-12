Just my first VSCode project setup using Joseph Fergusson's micro:bit extension for VSCode.

It gets the library stubs, and can flash to device.

To see extension output: output tab, then select microdot from the right.

Flashing: initially wasn't working. Output showed can't find 'ufs' command so I made a .bat file for it. It does try alternatives but only the .bat worked. Had to do same for uflash. 

Buildto copies MicroPython .hex file first, then reboots and drops main.py script to run. 
Put-this-file just copies the .py file to the code area (separate to USB disk area). 
One reboot main.py script is run by uPython hex system. 

USB serial post debugging works when you select USB com port. I think that blocks the flashing too...

And as I'm breadboarding things - need a way to version control that! Wokwi simulator sounds great for PI PICO but micro:bit not supported for simulation so no diagrams either. 

Fritzing https://fritzing.org/ seems to be kinda common, it's a standalone app an I paid €8 for the compiled WIndows version but it is FOSS. And people have created micro:bit diagrams: https://github.com/fritzing/fritzing-parts 

[CircuitCanvas](https://circuitcanvas.com/) looks great but the microbit imports are too big and I can't wrk out how to resize. I'm including PNGs as well as Fritzing file for those without the app. 
