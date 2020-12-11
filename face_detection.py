# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:43:28 2020

@author: Nagesh
"""

import cv2

cap = cv2.VideoCapture("video.mkv")

while True:
    if 0xFF and cv2.waitKey(100) == 27:
        break
    ret, img = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)[1]
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(cnts) != 0:
        cnts1 = max(cnts, key = cv2.contourArea)
        for c in [cnts1]:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cY = int(M["m01"] / M["m00"])
                l=[];
                for i in range(len(c)):
                    l.append(c[i][0][0])
            
                y1 = int(c[1][0][1])
                start_point = (min(l),y1)
                end_point = (max(l),cY+int(0.8*(cY-y1)))
                cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)
                cv2.imshow("Image", img)
                


cap.release()
cv2.destroyAllWindows()



