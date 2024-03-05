# Accident_detection
This repository contain Tensorflow lite model that detect (accident,fire) and it inference code.

## Main Objective:
Detect road accidents on drone camera using Raspberry pi and create report message then send it through LoRa network.

## Component
<li>Raspberry pi 4b (8 RAM)</li>
<li>LoRa Reyax rylr896 </li>
<li> Camera </li>

## Circuit Diagram
<img width="371" alt="image" src="https://github.com/HadiTeamProject/Accident_detection/assets/155265586/423ec904-6ea8-4820-b90b-500ab99cb420">

## Download Libraries
 
```bash
pip install opencv-python
pip install tensorflow==2.13.1
pip install tflite_support==0.4.3
```

### Notes
<li> download the tensorflow model from here 
https://drive.google.com/file/d/19cyicJl726NxIpRvRjAofu5KdxKyYKga/view?usp=drive_link

</li>
<li>use Thonny IDE </li> 
<li>LoRa address is 2</li>
<li>LoRa network is 2</li>
<li>LoRa band is 915 MHz</li>
<li>LoRa braud rate is 9600 </li>
