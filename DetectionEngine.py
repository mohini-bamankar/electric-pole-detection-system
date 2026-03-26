import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2
from ultralytics import YOLO
import random
import WhatsAppAPI
from threading import Thread
import os
import Electric_Pole_status
import operator
import collections
import time
from mutagen.mp3 import MP3
import pygame
import EMAILSender
    
    
def playAlert():
    audio_file = "danger_alert.mp3"
    audio = MP3(audio_file)
    duration = audio.info.length
    
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(duration+2)
    
cap = cv2.VideoCapture(2)    
    
def startEngine(latitude,longitude,mobile,email):
        
    model = YOLO("model/best.pt")

    cappath="Captured_images"


    if not os.path.exists(cappath):
        os.makedirs(cappath)  
   
  
    
    
    
    # if not cap.isOpened():
    #     print("Cannot open camera")
    #     exit()
    count=0 
    imagenum=0
    classnamelist=[]
    getNotify = 0
    while True:
        ret, frame = cap.read()
    
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        print("IN frame")
        dim = (1000, 600)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
        if(Electric_Pole_status.getStatus()==1):
            if getNotify == 0:
                whatsappThread = Thread(target = WhatsAppAPI.send_whatsapp_msg, args = (latitude,longitude,mobile))
                whatsappThread.start() 
                
                
                emailThread = Thread(target = EMAILSender.send_mail(email, latitude, longitude), args = (latitude,longitude,mobile))
                emailThread.start() 
                
                getNotify = 1
                
            detect_params_human = model.predict(source=[frame], conf=0.1, save=False)
            
        
          
            for box in detect_params_human[0].boxes:
                clsID = box.cls.numpy()[0]
                conf = box.conf.numpy()[0]
                bb = box.xyxy.numpy()[0]
            
                x1 = int(bb[0])
                x2 = int(bb[2])
                y1 = int(bb[1])
                y2 = int(bb[3])
               
                 
                
                class_text = model.names[clsID] 
                value=round(conf, 3)
                
                if(value>=0.9):
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.putText(frame, f"{class_text}_{value:.2f}", (x1, y1), font, 1, (0, 0, 255), 2)
                    print(" count  === " ,count)
                    count=count+1
                    if count >=5:
                        playAlert()
                        count=0
                        
                        
                        
                        
                        
                        
                
        
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow('Human presence Detection System', frame)
            
    
            
    
    # Release the capture and destroy all windows
   # cap.release()
   # cv2.destroyAllWindows()

#startEngine("text")

