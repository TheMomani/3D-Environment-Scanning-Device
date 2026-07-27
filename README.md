# 3D-Environment-Scanning-Device
## Description:

Embedded C Firmware + Python visualization system which utilizes an ARM Cortex-M4 MCU, VL53L1X Time of Flight sensor, and a stepper motor into a 3D environment scanner, reconstructing physical rooms into 3D interactive point cloud plots.

--------------------------------

## Overview:

The system operates by using a stepper motor to incrementally rotate the sensor in a 360o scan, where the sensor collects distance readings between increments, resulting in multiple distance values across angle increments in the scan. These 360o scans, which will be referred to as “slices”, are then repeated multiple times as the device is moved, to generate a 3D model of the surroundings with many slices.
The distance data is collected from the sensor via I2C at 100kbps and then transferred to the PC from the MCU using UART at 115200 baud formatted as CSV. A Python-based program then receives the data and processes it, handling anomaly detection and scaling, to construct an interactive 3D model by converting polar measurements into Cartesian coordinates using trigonometric equations.

--------------------------------

## Key Specifications:

![Characteristic Table](/3D-Environment-Scanning-Device/Images/charTable.png)

--------------------------------

## Functionality:

### Firmware (MCU):

Initialises the system clock and sensor, then pulls onboard buttons to begin or end scanning. The stepper motor is rotated 360deg incrementially, with the ToF sensor taking the average of 5 distance measurements (between motor rotation increments). The MCU transmits the required data in CSV format to the PC via UART. A flowchart is shown below, since the full MCU firmware source code is not publicly displayed to avoid academic integrety policies.

![C program flowchart](../3D-Environment-Scanning-Device/Images/mainCFlow.png)


### Python Visualization (PC):

