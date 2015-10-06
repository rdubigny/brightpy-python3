# BrightPy for Python 3 and Linux raspberrypi 4.1.10-v7+ firmware

This is a reworking of [BrightPi Python Module](https://brightpi.codeplex.com/SourceControl/latest#readme.txt) so it works with python 3 and the latest RaspberryPi firmware.

## Raspberry setup

Uncomment the following in `/boot/config`

    dtparam=i2c_arm=on
    
Then add the following line to `\etc\modules`

    snd-bcm2835
    i2c-dev
    i2c-bcm2708
    
Install IC2 utilities:

    sudo apt-get install python3-smbus i2c-tools

Finally reboot your raspberry.

## Run

    sudo python3 test1
    
## Documentation

https://www.pi-supply.com/bright-pi-v1-0-code-examples/
http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/io-pins-raspbian/i2c-pins
https://brightpi.codeplex.com/SourceControl/latest
https://raspberrypi.stackexchange.com/questions/27073/firmware-3-18-x-breaks-i%C2%B2c-spi-audio-lirc-1-wire-e-g-dev-i2c-1-no-such-f
http://pi.gadgetoid.com/pinout
