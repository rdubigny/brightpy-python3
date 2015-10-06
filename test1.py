import BrightPILed
import time

try:
    light = BrightPILed.BrightPI(1)
    print("YOLO??")
    light.reset()
    light.led_1_on()
    time.sleep(0.5)
    light.led_2_on()
    time.sleep(0.5)
    light.led_3_on()
    time.sleep(0.5)
    light.led_4_on()
    time.sleep(0.5)
    light.led_4_off()
    time.sleep(0.5)
    light.led_3_off()
    time.sleep(0.5)
    light.led_2_off()
    time.sleep(0.5)
    light.led_1_off()
    time.sleep(0.5)
    light.led_all_on()
    time.sleep(0.5)
    for x in range(0, 64):
        light.led_all_brightness(64 - x)
        time.sleep(0.1)
    light.led_all_off()
except Exception as e:
    print(e)
