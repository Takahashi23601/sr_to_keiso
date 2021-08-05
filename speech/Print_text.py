import cv2
import numpy as np
import tkinter

def Print_text(img,text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,text,(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
    


