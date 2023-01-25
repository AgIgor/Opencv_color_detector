import cv2
import numpy as np
import matplotlib.pyplot as plt

# cap = cv2.VideoCapture('collors.png')
cap = cv2.VideoCapture('hd.mp4')
# cap = cv2.VideoCapture(0)

start_point = (101, 101)
end_point = (529, 249)
color = (0, 0, 0)
thickness = -1

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    fps = int(cap.get(5))
    frame_count = cap.get(7)
    # print("Frame Rate : ", fps, "frames per second"," Frame count : ", frame_count)

    ret, frame = cap.read()
    h, w = frame.shape[:2]
    # print(h, w)

    if ret:
        # frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

        # frame = cv2.rectangle(frame, (0, 0), (100, 100), (0, 255, 0), -1)
        # frame = cv2.rectangle(frame, (0, 250), (10, 10), (0, 255, 0), -1)

        cv2.imshow('Frame', frame)
        # (b, g, r) = frame[0, 0]
        # print(h, w, r, g, b)

        for p in range(0, h, 100):
            (b, g, r) = (frame[0, p])
            print(f'{h},{w} [{r},{g},{b}]')

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
