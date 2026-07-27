Features:


- 3D scanning system using Time-of-Flight distance sensing

- Uses VL53L1X for accurate distance measurement from 0mm to 4000mm

- 360° rotational scanning using stepper motor (2048 steps/rev)

- Multi-slice scanning for basic 3D reconstruction of surroundings

- UART communication with PC for real-time data streaming

- Python-based visualization logic for 3D plot generation

- Button-controlled operation (start/stop scanning)

- Onboard LED indicators for system status and activity

- Averaging filter (5 samples) to reduce measurement noise

- Anomaly value detection while plotting 3D reconstruction

- Task-based design (scan / return / pause)

- Operates at 10 MHz system clock (PLL configured)

- 3.3V for ToF sensor, 5V for motor

- Uses I2C at 100 kbps and UART at 115200 baud

- Powered using 3.3V (sensor) and 5V (motor driver)

- PC-side processing implemented in Python (Matplotlib, Serial)

- Embedded system runs on MSP432E401Y MCU with on-chip memory

- Estimated system cost: ~$25–$40 (sensor + motor + driver), $100 with MCU ($60)


Characteristic Table:

![Characteristic Table](../Images/charTable.png)
Above is a charactertic table, highlighting the specifications of the individual components used, as well as important specs of the system.