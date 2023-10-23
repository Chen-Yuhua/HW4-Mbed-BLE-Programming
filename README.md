# HW4-Mbed-BLE-Programming

Group : 9  
Member : B09901043 陳昱樺 B09901134 林容丞

Function
---
Here are what this project does:
1. Implement BLE programming. Let STM32 be the server and RPi be the client.
2. Provide two services, heartrate and magnetometer.
3. Heartrate is simulated, which will increase by 1 per second. Its range is from 60 bpm to 110 bpm.
4. Magnetometer 3D values are detected by STM32 sensor, which will update once a second.
5. STM32 will connect to RPi using BLE.
6. RPi will print the values of heartrate and magnetometer in the console.

Prerequisites
---
There are four things a user should prepare to run this project:
* Android phone with app BLE Scanner.
* STM32 development board
* Raspberry Pi 3
* Python

Usage
---
Here are some steps to run this project properly:
1. Import the project into Mbed Studio.
2. Update headerfiles such as MagnetoService.h and GattCharacteristic.h.
3. Move central.py into RPi.
4. Run main.cpp in Mbed Studio.
5. Run central.py in RPi.
6. Heartrate and magnetometer values are shown in the console.

License
---
None.

Acknowledgements
---
Here are some resources we refer to to finish this project:
* Course slides: Porting a Project to the Mbed Studio.pdf
* Course video: [Demo] BLE_GattServer_AddService demo-heart rate notifications.ecm.mp4
