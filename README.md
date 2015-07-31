# Real-time Subway Countdown
Please visit http://chris-griffin.github.io/real-time for more information. 

## Usage

This repository allows you to run a countdown clock for the NYC Subway from the comfort of your own apartment, home or office. You can configure it to display the times for the exact train(s)/station(s) you desire. It runs via RGB LED panels, the Raspberry Pi 2, @hzeller's great [RGB LED library](https://github.com/hzeller/rpi-rgb-led-matrix), and the MTA's real time API. 

[![Demo Video](http://img.youtube.com/vi/jUFrGG-O-hE/0.jpg)](http://www.youtube.com/watch?v=jUFrGG-O-hE)

## Requirements

### Hardware

While the cheapest option to source the hardware necessary for the project is likely Alibaba.com, it generally requires a lot of lead time. To get up and running quickly, I recommend [Adafruit](https://www.adafruit.com/).

Female DC Power adapter - 2.1mm jack to screw terminal block
Premium Female/Female Jumper Wires - 40 x 6"

5V 4A (4000mA) switching power supply - UL Listed Medium 16x32 RGB LED matrix panel x 2 

Miniature WiFi (802.11b/g/n) Module: For Raspberry Pi

Raspberry Pi 2 - Model B - ARMv7 with 1G RAM

5V 2A Switching Power Supply w/ 20AWG 6' MicroUSB Cable

4GB SD card for Raspberry Pi preinstalled with Raspbian Wheezy

Optional: 

USB or wireless mouse/keyboard, HDMI cable, and display for initial Raspberry Pi setup

Mounting hardware

### Software

In addition to a fresh install of Raspbian, you will need to install these libraries:

[PIL](http://www.pythonware.com/products/pil/)

[gtfs-realtime-bindings](https://developers.google.com/transit/gtfs-realtime/code-samples?hl=en#python)

@hzeller's [RBG LED library](https://github.com/hzeller/rpi-rgb-led-matrix). Make sure to install this in the same folder as this repository.

## Installation

TODO: Describe the installation process

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
