import cv2
import mediapipe as mp
import pyautogui
import win32api
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from math import sqrt
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click=0
video = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.5) as hands:
  while video.isOpened():
    _,frame = video.read()
    image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    image= cv2.flip(image,1)
    imageHeight,imageWidth, _ = image.shape
    results = hands.process(image)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for num,hand in enumerate(results.multi_hand_landmarks):
        mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(250,44,250),thickness=2,circle_radius=2),)
    if results.multi_hand_landmarks!=None :
      for handLandmarks in results.multi_hand_landmarks:
        for point in mp_hands.HandLandmark:
          normalizedLandmark=handLandmarks.landmark[point]
          pixelCoordinatesLandmark=mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,normalizedLandmark.y,imageWidth,imageHeight)
          point = str(point)
          if point == 'HandLandmark.INDEX_FINGER_TIP':
            try :
              indexfingertip_x=pixelCoordinatesLandmark[0]
              indexfingertip_y=pixelCoordinatesLandmark[1]
              win32api.SetCursorPos((indexfingertip_x*4,indexfingertip_y*5))
            except:
              pass
          elif point =='HandLandmark.THUMB_TIP':
            try:
                thumbfingertip_x=pixelCoordinatesLandmark[0]
                thumbfingertip_y=pixelCoordinatesLandmark[1]
                #print("thumb",thumbfingertip_x)
            except:
                pass
          elif point =='HandLandmark.MIDDLE_FINGER_TIP':
             try:
                middlefingertip_x=pixelCoordinatesLandmark[0]
                middlefingertip_y=pixelCoordinatesLandmark[1]
                #print("thumb",thumbfingertip_x)
             except:
                 pass
          elif point =='HandLandmark.RING_FINGER_TIP':
             try:
                ringfingertip_x=pixelCoordinatesLandmark[0]
                ringfingertip_y=pixelCoordinatesLandmark[1]
                #print("thumb",thumbfingertip_x)
             except:
                 pass
                
        try:
            #pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
            Distance_x=sqrt((thumbfingertip_x-indexfingertip_x)*2 +(thumbfingertip_x-indexfingertip_x)*2)
            Distance_y=sqrt((thumbfingertip_y-indexfingertip_y)*2 +(thumbfingertip_y-indexfingertip_y)*2)
            #print("X",Distance_x)
            #print("Y",Distance_y)
            if Distance_x<10 and Distance_y<10:
                click=click+1
                if(click%5==0):
                    print("left click")
                    print("X",Distance_x)
                    print("Y",Distance_y)
                    pyautogui.click(button='left')
        except:
            pass
        try:
            #pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
            Distance_x=sqrt((thumbfingertip_x-middlefingertip_x)*2 +(thumbfingertip_x-middlefingertip_x)*2)
            Distance_y=sqrt((thumbfingertip_y-middlefingertip_y)*2 +(thumbfingertip_y-middlefingertip_y)*2)
            if Distance_x<10 and Distance_y<8:
                click=click+1
                if(click%5==0):
                    print("right click")
                    print("X",Distance_x)
                    print("Y",Distance_y)
                    pyautogui.click(button='right')
        except:
            pass
        try:
          #pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
          Distance_x=sqrt((indexfingertip_x-middlefingertip_x)*2 +(indexfingertip_x-middlefingertip_x)*2)
          Distance_y=sqrt((indexfingertip_y-middlefingertip_y)*2 +(indexfingertip_y-middlefingertip_y)*2)
          print("X",Distance_x)
          print("Y",Distance_y)
          if Distance_x<10 and Distance_y<10:
              print("click")
              print("X",Distance_x)
              print("Y",Distance_y)
              pyautogui.scroll(-40)
        except:
            pass
        try:
          #pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
          Distance_x=sqrt((indexfingertip_x-middlefingertip_x)*2 +(indexfingertip_x-middlefingertip_x)*2)
          Distance_y=sqrt((indexfingertip_y-middlefingertip_y)*2 +(indexfingertip_y-middlefingertip_y)*2)
          #print("X",Distance_x)
          #print("Y",Distance_y)
          if Distance_x>=10 and Distance_y<10:
              print("hhclick")
              print("X",Distance_x)
              print("Y",Distance_y)
              pyautogui.scroll(40)
        except:
            pass
    cv2.imshow('Hand Tracking' , image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
video.release()
cv2.destroyAllWindows()
