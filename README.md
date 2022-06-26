# Trash Classifier Example Project

<!-- 
Guidelines on README format: https://review.docs.microsoft.com/help/onboard/admin/samples/concepts/readme-template?branch=master

Guidance on onboarding samples to docs.microsoft.com/samples: https://review.docs.microsoft.com/help/onboard/admin/samples/process/onboarding?branch=master

Taxonomies for products and languages: https://review.docs.microsoft.com/new-hope/information-architecture/metadata/taxonomies?branch=master
-->

<img src="images/Cover-5.jpg" width="400">

The Trash Classifier project, affectionately known as "Where does it go?!", is designed to make throwing things away faster and more reliable. 

The Trash Classifier project uses a Machine Learning model trained in [Lobe](https://github.com/lobe) to identify whether an object goes in the garbage, recycling, compost, or hazardous waste. The model is then loaded onto a Raspberry Pi computer to make it usable wherever you might find rubbish bins! 

This ReadMe shows you how to create your own Trash Classifier project on a Raspberry Pi from a Lobe TensorFlow model in Python3.

## Contents

This repository contains the following files:

| File/folder               | Description                                |
|---------------------------|--------------------------------------------|
| `images`                  | Folder containing images for this project  |
| `tests`                   | Folder containing tests for connections    |
| `rpi_trash_classifier.py` | Trash Classifier Sample Code for the Pi    |
| `README.md`               | This README file!                          |
| `LICENSE`                 | The license for the sample.                |

## Prerequisites
This project assumes you are starting with a WiFi-connected headless Raspberry Pi 4 pre-loaded with Raspbian. We recommend using the desktop version of Raspbian so you can see images captured by the Pi camera.

You'll need to access the Pi remotely via SSH, which requires either a local WiFi connection or an Ethernet cable. Please see [this repo](https://github.com/microsoft/rpi-resources) for more information on how to setup the Pi for remote, or headless, connection.

### Background Knowledge
To build this project successfully, you should have some prior knowledge of:
* Linux OS via SSH
* Accessing the Pi's desktop remotely
* Basic Python skills (e.g. how to read and edit Python code)
* How to read wiring diagrams and use a breadboard

### Software (PC-side)
* Lobe
* [WinSCP](https://winscp.net/eng/index.php) (or other SSH file transfer method, can use [CyberDuck](https://cyberduck.io/) for Mac)
* Terminal  
* Remote Desktop Connection or RealVNC

### Hardware
* Raspberry Pi, SD Card, and USB-C power supply (5V, 2.5A)
* Pi Camera
* Pushbutton
* 5 LEDs (4 indicator LEDs and 1 status LED)
    * Yellow LED: garbage
    * Blue LED: recycle
    * Green LED: compost
    * Red LED: hazardous waste
    * White LED: status 
* 6 220 Ohm resistors
* 1 JST connector, female end only
* 2 M-to-F jumper wires
* 10 F-to-F jumper wires
* Breadboard, half-size
* PCB (optional but recommended ideal)

### Enclosure
* Project case (e.g. cardboard, wood, or plastic box)
* 0.5" x 0.5" (2cm x 2cm) clear plastic square 
* Velcro

### Tools
* Wire cutters
* Precision knife (e.g. exacto knife) and cutting mat
* Soldering iron (ideal)
* Hot melt tool (or other non-conductive glue -- epoxy works great but is 100% permanent)

## Setup
1. Export your Lobe ML model in a TensorFlow Lite (TF Lite) format. 
2. On your PC, open WinSCP and connect to your Pi. Create a *Lobe* folder in your Pi's home directory and create a *model* folder in that directory. Drag the resulting Lobe TF Lite folder contents onto the Pi. Note the file path: /home/pi/Lobe/model
3. At the moment, Lobe doesn't install TensorFlow Lite Runtime properly. The issue is being tracked here: [lobe/lobe-python#11](https://github.com/lobe/lobe-python/issues/11). To workaround this, on the Pi, open a terminal and download tflite-runtime for Python3:
    ```sh
    pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
    ```
4. On the Pi, open a terminal and download the [lobe-python library](https://github.com/lobe/lobe-python) for Python3:
    ```sh
    pip3 install lobe
    ```

5. Download this repo onto the Pi (or download onto your PC and send the example python code to the Pi via WinSCP).
6. Carefully connect the Pi Camera to Pi (visit the [Pi Foundation getting started guide](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/1) for more information).
7. Follow the wiring diagram below to connect the pushbutton and LEDs to the Pi GPIO pins.

<img src="images/WhereDoesItGo_bb.jpg" width="400">

## Running the sample
Once you've connected the hardware to the Pi's GPIO pins, read through the example code and update any file paths as needed:
* Line 29: filepath to the Lobe TF Lite model directory
* Lines 47 and 83: filepath to captured images via Pi Camera

Run the program using Python3 in the terminal window:
    ```
        python3 rpi_trash_classifier.py
    ```

### Program Overview
When you first run the program, it will take some time to load the TensorFlow library and the Lobe ML model. When the program is ready to capture an image, the status light (white LED) will pulse.

Once you've taken an image, the program will compare the image to the Lobe ML model and output the resulting prediction (line 83). The output determines which light is turned on: yellow (garbage), blue (recycle), green (compost), or red (hazardous waste). 

If none of the indicator LEDs turn on and the status LED returns to pulse mode, it means that the image captured was "not trash", in other words, retake the photo!

### Capturing an Image
Press the pushbutton to capture an image. Note that you may need to hold the pushbutton for at least 1s for the program to register the press. It is recommended to take some test images, then open them on the Desktop to better understand the camera view and frame. 

To allow the user time to position the object and for camera light levels to adjust, it takes about 5s to fully capture an image. You may change these settings in the code (lines 35 and 41), but keep in mind the Pi Foundation recommends a minimum of 2s for light level adjustment.

### Testing and Troubleshooting
Before you solder or make any of the connections permanent, be sure to test the code with the hardware. For example, in the tests/ directory there are some examples that can be run to verify that each component used in the main program (LEDs, the TF model, the button and the camera) is working as it was intended to.

The biggest challenge is ensuring that the captured image is what we expect, so take some time to review the images and compare expected results with indicater LED output. If necessary, you can pass in images to the Lobe ML model for direct inferencing and faster comparison.

A few things to note: 
* The TensorFlow library will likely throw some warning messages -- this is typical for the version used in this sample code.
* The prediction labels must be exactly as written in the led_select() function, including capitalization, punctuation, and spacing. Be sure to change these if you have a different Lobe model.
* The Pi requires a steady power supply. The Pi's power light should be bright, solid red.
* If one or more LEDs are not turning on when expected, check by forcing them on with the command:
    ```
        red_led.on()
    ```

## Build the Enclosure
Create an enclosure for your Pi that will hold the camera, pushbutton, and LEDs in place while also protecting the Pi. 

Design your own enclosure or follow our build instructions below for quickly prototyping a cardboard enclosure!

(Enclosure build instructions coming soon!)

## Finalize and Install!
When you've successfully tested the program and its hardware, you're ready to finalize your build! Solder components and coat in glue or epoxy to hold them in place. Note that if you choose to use epoxy, you may not be able to use the Pi's GPIO pins for other projects in the future. If you're concerned about this, add in a GPIO ribbon cable and connect the jumper wires to that instead.

Place the enclosure about your trash bins and run the program to get a faster, more reliable way of reducing our waste!

## Questions, Ideas, and Contributing

Questions about or ideas for this project? Please let us know! We are always looking to improve our sample code and documentation.

This project also welcomes contributions and suggestions.  Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
