import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import time
import serial

model = AccidentDetectionModel("tf_lite1_model_new.tflite") 
font = cv2.FONT_HERSHEY_SIMPLEX
cmsg=""

def startapplication():
    # Set LoRa variable
    lora = serial.Serial(port='/dev/serial0',baudrate=9600,timeout=1)    
    
    #capture camera videos
    video = cv2.VideoCapture(0)
    
    while True:
        #save video frame as img
        ret, frame = video.read()
        roi = cv2.resize(frame, (250, 250))
        
        #predict each image using tflite model
        pred, prob = model.predict_accident(roi)

        #make sure probababilty is above 99% 
        if prob[0][np.argmax(prob)] > 0.99:

            #Display the result and its probababilty 
            cv2.rectangle(frame, (0, 0), (300, 50), (0, 0, 0), -1)
            cv2.putText(frame, f"{pred}: {round(prob[0][np.argmax(prob)] * 100, 2)}%", (20, 30), font, 1, (255, 255, 0), 2)

            #depend on model result prepare the msg
            #GPS coordinate is missing  
            if pred == 'Accident':
                msg = "2" 
            elif pred == 'Fire':
                msg = "3"
            else:
                msg = "1"
            #to elimate msg repeat
            if cmsg != msg:
                cmsg=msg
                gps_coor= "22,33" #should modify the msg to include the real GPS coordinate once it is connected to the drone
                
                #LoRa send command form
                smsg = f'AT+SEND=1,7,{cmsg},{gps_coor}\r\n'

                #msg should be in byte formate
                bmsg = smsg.encode('utf-8')
                lora.write(bmsg)
                time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return None
        frame = cv2.resize(frame,(1000,600))
        cv2.imshow('Video', frame)

if __name__ == '__main__':
    startapplication()
