import cv2
from pyzbar.pyzbar import decode
import numpy as np
#image = cv2.imread('3.jpg')
cap = cv2.VideoCapture(0)


while True:
    success,frame = cap.read()
    barcode = decode(frame)
    for code in barcode:
        pts = np.array([code.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(frame, [pts], True, (255,0,255) )
        text_pts = code.rect
        barcode = code.data.decode('utf-8')
        cv2.putText(frame, barcode, (text_pts[0], text_pts[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255))
        print(barcode)
    cv2.imshow("Test", frame)
    cv2.waitKey(1)
