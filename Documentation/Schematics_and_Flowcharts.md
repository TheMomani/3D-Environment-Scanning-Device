Below are flowcharts and diagrams giving a high-level visualisation of the entire system


![Flowchart of main C program](../Images/mainCFlow.png)
While the source firmware files are not included due to potential course academic integrity infringement, the above flowchart gives a general idea on how the embedded C on the MCU works. Initialising the system clock, ToF sensor, and then polling for button inputs and operating the sensor + motor at the same time. No magic numbers are used, and the settings can be altered by the user by modifying the defined constants. 


![Flowchart of Python visualization program](../Images/PyFlow.png)
Above is the flowchart for the PC program built using Python's Serial, MatPlotLib, and Math libraries. The program receives CSV data sent over UART, parses it, detects and flags anomalies, then creates a live 3D render of the scans together. The code is provided under the folder "Python Visualization" and the results are under the folder "Results".


![System Schematic](../Images/systemScheme.png)
The above figure shows how the hardware of the system is connected together.


![Block Diagram](../Images/BlockDiagram.png)
The above figure displays how data is transmitted and received