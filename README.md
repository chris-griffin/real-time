# Real-time Subway Countdown Display

## Usage

This repository allows you to run a countdown clock display for the NYC Subway from the comfort of your own apartment, home or office. You can configure it to display the times for the exact train(s)/station(s) you desire. It runs via RGB LED panels, the Raspberry Pi 2, @hzeller's great [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix), and the MTA's real time API. Currently, the MTA currently only disseminates real-time data for the "A" division trains which include the 1, 2, 3, 4, 5, 6 and L trains, and as a result are the only lines supported. For avoidance of doubt, this repository is in no way connected, endorsed, or licensed by the Metropolitan Transportation Authority ("MTA"). 

**Please note that these panels do not have built-in PWM control and therefore should be run by a real-time processor. This repository utilizes the Raspberry Pi which is not a real-time processor. With that said, there should be limited issues utilizing the Pi to drive two RGB LED matrix panels. The performance issues should be limited to slight artifacts in the image including some "static" which can be seen below. You may be interested in exploring the use of level-shifters, real-time Linux kernels, or a [real-time HAT](http://www.adafruit.com/products/2345), but these are currently untested.**

You can see a demo of the completed display on [YouTube](https://www.youtube.com/watch?v=BXbsdpKbUQQ)
[![Demo Video](https://img.youtube.com/vi/BXbsdpKbUQQ/0.jpg)](https://www.youtube.com/watch?v=BXbsdpKbUQQ)

## Requirements

### Hardware

While the cheapest option to source the hardware necessary for the project is likely Alibaba.com, it generally requires a lot of lead time. To get up and running quickly, I recommend [Adafruit](https://www.adafruit.com/). I have provided links to the exact products I purchased from Adafruit.

* [Raspberry Pi 2 - Model B](https://www.adafruit.com/products/2358)
* [Mini USB WiFi Module](https://www.adafruit.com/products/814)
* [4GB SD Card (Optionally Preinstalled with Raspbian Wheezy)](https://www.adafruit.com/products/1121)
* [5V 2A Power Supply w/ MicroUSB Cable](https://www.adafruit.com/products/1995)
* [2 16x32 RGB LED Matrix Panels](https://www.adafruit.com/products/420)
* [Female DC Power Adapter - 2.1mm Jack to Screw Terminal Block](https://www.adafruit.com/products/368)
* [5V 4A Power Supply](https://www.adafruit.com/products/1466)
* Solder/Insulated Wire (if you own a soldering iron) OR [Premium Female/Female Jumper Wires](https://www.adafruit.com/products/266)
* USB or wireless mouse/keyboard, HDMI cable, and display (all for initial Raspberry Pi setup)
* Mounting hardware
* Wire Stripper/Cutter

### Software

In addition to a fresh install of [Raspbian](https://www.raspbian.org/), you will need to install these libraries:

* [PIL](http://www.pythonware.com/products/pil/)
* [python gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/code-samples?hl=en#python)
* @hzeller's [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix). Make sure to install this in the empty "rpi-rgb-led-matrix" directory in this repository.

## Installation

1. Get the Raspberry Pi up and running. 
   * If you didn't get an SD card with Raspbian pre-installed, download the [latest image](https://www.raspberrypi.org/downloads/) and follow the appropriate [installation guide](https://www.raspberrypi.org/documentation/installation/installing-images/). 
   * Connect the Raspberry Pi to a keyboard, mouse, and display. Insert the SD card. Insert the MicroUSB power adapter and wait for the system to boot. If the system does not boot, check this guide for [troubleshooting](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=28&t=58151). 
   * Login to the Pi if prompted using the default username "pi", and the default password "raspberry". 
   * Configure the Pi using the "raspi-config" configuration screen which should automatically launch. If not use `sudo raspi-config` to access the menu. Make sure to change the timezone to New York and to change the default password before connecting to the internet. I also recommend using SSH to connect to the Pi remotely going forward. For more detailed information on the menu, please use this [guide.](https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
   ![Raspi-Config Menu](http://www.blogcdn.com/www.engadget.com/media/2012/08/expandrootfsopt1.png)
   * Update the packages
   ```
   sudo apt-get update
   sudo apt-get upgrade
   ```
   * Safely shutdown the system with `sudo shutdown -h now` and then unplug the power. 
   * Insert the USB WiFi adapter and boot up the system. Enter the GUI via `startx` and [configure the WiFi](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-raspbian).
2. With both the RGB LED matrices and Raspberry Pi disconnected from power, connect the two using the female to female wires OR solder. Either way, use following the [wiring diagram](https://github.com/hzeller/rpi-rgb-led-matrix#wiring-diagram), and make sure you are wiring to the input side of one of the RGB LED panels. To connect the two matrices together, simply use the IDC cable as pictured below.

![Wiring Example](http://i.imgur.com/lcoUGVK.jpg)

3. In order to connect the panels to a power source, I had to cut one end of the AMP style power cords above the plastic piece, strip the insulation off the last 1/2" of the wires, and connect them to screw terminal DC power adapter. Make sure you have the polarity of the wires correct. The red wires on my panels went to the positive (+) side of the screw terminals and the blue wires went to the negative (-) side. Make sure to handle the connection with care and I suggest wrapping it in electrical tape for safety and stability. 

4. With the matrices correctly wired to the Pi and connected to power, boot the Pi back on. Login using your new credentials, and navigate to the GUI via `startx`. Make sure you are connected to the internet, and open up the command prompt. Create a directory named "subwaydisplay" via `mkdir subwaydisplay` and navigate to the directory via `cd subwaydisplay`. Clone this repository into the folder via `git clone https://github.com/chris-griffin/real-time.git`. If you run into an error, make sure that you have git installed via `sudo apt-get install git`. Navigate to the "rpi-rgb-led-matrix" directory via `cd rpi-rgb-led-matrix` and clone @hzeller's [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix) via `git clone https://github.com/hzeller/rpi-rgb-led-matrix.git`. Run the `make` command to compile the files of this repository. 

5. Install [PIL](http://www.pythonware.com/products/pil/) and [python gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/code-samples?hl=en#python) via instructions from the provided links. 

6. Obtain a developer key from the [MTA](http://web.mta.info/developers/developer-data-terms.html) and update the "sampleconfig.py" file with this information. Rename this file to "config.py".


6. Navigate back to the "subwaydisplay" directory in the command prompt and run the "importdata.py" program with `python importdata.py`. You should see the RGB LED matrix panels come to life with the information for the uptown and downtown Wall Street 2/3 trains, and downtown 4/5 trains. You can adjust which trains are displayed by altering the config file with the appropriate station ids which can be found in the "StaticData" folder. 



## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License

The MIT License (MIT)

Copyright (c) 2015 Christopher Griffin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
