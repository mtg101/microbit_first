from microbit import *

while True:
    display.show(Image.HEART)

    sleep(100)

    if button_a.was_pressed():
        display.show(Image.ARROW_E)
        print("Button A")
        sleep(500)

    if button_b.is_pressed():
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)


    