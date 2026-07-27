# 3D-Environment-Scanning-Device
Description:


The device uses a VL53L1X Time of Flight (ToF) sensor, an MSP432E401Y microcontroller (MCU), and a stepper motor to capture surrounding distance data, and build a 3D model of the environment on an interactive plot in the x, y, and z axes.
The system operates by using a stepper motor to incrementally rotate the sensor in a 360o scan, where the sensor collects distance readings between increments, resulting in multiple distance values across angle increments in the scan. These 360deg scans, which will be referred to as “slices”, are then repeated multiple times as the device is moved, to generate a 3D model of the surroundings with many slices.
The distance data is collected from the sensor via I2C at 100kbps and then transferred to the PC from the MCU using UART at 115200 baud formatted as CSV. A Python-based program then receives the data and processes it, handling anomaly detection and scaling, to construct an interactive 3D model by converting polar measurements into Cartesian coordinates using trigonometric equations
