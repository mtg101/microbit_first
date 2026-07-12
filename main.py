from microbit import *

while True:
    display.show(Image.HEART)

    sleep(100)

    if button_a.was_pressed():
        display.show(Image.ARROW_E)
        print("Button A")
        sleep(500)


    