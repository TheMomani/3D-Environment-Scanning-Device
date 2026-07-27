import serial 
import math 
import matplotlib.pyplot as plt 

s = serial.Serial('COM4', 115200) 
print("Connected. Waiting for data...") 

# Settings 
angleScan = 11.25 # angle of increment?
pointsPerSlice = 32 # How many scans per slice?
numSlices = 1 # How many slices will be scanned?

fig = plt.figure(figsize=(12, 10)) 
ax = fig.add_subplot(111, projection='3d') 

total_scan_data = [] 

for sliceCount in range(numSlices): 
    XList, YList, ZList = [], [], [] 
    anomaly = False 
    for i in range(pointsPerSlice): 
        line = s.readline().decode('utf-8').strip() 
        try:
            displacement, angle_idx, distance = map(float, line.split(','))
            print(line)

            angle_rad = math.radians((angle_idx * angleScan)) -math.radians(7) # 7 degree offset since the motor keeps lagging, leading to twisted 3D reconstructions
            if(distance>3500 or distance < 50):
                distance = 4000
                anomaly = True
            else:
                anomaly = False
                
            x = displacement
            y = distance * math.sin(angle_rad)
            z = distance * math.cos(angle_rad)

            
            XList.append(x)
            YList.append(y)
            ZList.append(z)

            if(not anomaly and i==0):
                ax.scatter(x, y, z, color='green', s=5) #To see where the first point is on the slice
            elif(not anomaly and i>0):
                ax.scatter(x, y, z, color='blue', s=5) #Sensible point is plotted in blue
            else:
                ax.scatter(x, y, z, color='red', s=5) #Faulty point is plotted in red
            if i == 0: 
                ax.scatter(x, 0, 0, color='black', s=5) #To easily find the origin

            ## Using the first point and the origin, we are able to orient the graph correctly based on the starting position of the motor


            
                

        except ValueError:
            print(f"Skipping: {line}")

    # Close the ring
    if len(XList) > 0:
        XList.append(XList[0])
        YList.append(YList[0])
        ZList.append(ZList[0])
        ax.plot(XList, YList, ZList, color='blue', linewidth=2, alpha=0.5)

    total_scan_data.append(list(zip(XList, YList, ZList)))

# Grey lines connecting same point index across slices
for pointNumber in range(pointsPerSlice):
    lx, ly, lz = [], [], []
    for sliceCount in range(numSlices):
        if pointNumber < len(total_scan_data[sliceCount]):
            p = total_scan_data[sliceCount][pointNumber]
            lx.append(p[0])
            ly.append(p[1])
            lz.append(p[2])
    ax.plot(lx, ly, lz, color='blue', linewidth=0.5, alpha=0.3)

s.close()

ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.title('3D Scan')
plt.show()
