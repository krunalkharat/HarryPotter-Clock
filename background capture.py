# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:47:51 2020

@author: KRUNAL
"""

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret , back = cap.read()
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord("q"):
            cv2.imwrite("image.jpg",back)
            break
        
cap.release()
cv2.destroyAllWindows()