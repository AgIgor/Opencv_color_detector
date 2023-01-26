import cv2

# cap = cv2.VideoCapture('collors.png')
cap = cv2.VideoCapture('hd.mp4')
# cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")

while cap.isOpened():
    # fps = int(cap.get(5))
    # frame_count = cap.get(7)
    # print("Frame Rate : ", fps, "frames per second"," Frame count : ", frame_count)
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1280, 720))
    h, w = frame.shape[:2]
    # print(f'h = {h}, w = {w}')

    if ret:
        # time.sleep(.07)
        # leds_side = 35

        led_pos_inicio = 25
        for i in range(0, 700, 50):

            (b, g, r) = (frame[led_pos_inicio + 10 + i, led_pos_inicio])# # \/ , >

            frame = cv2.rectangle(frame, (10 - 1, led_pos_inicio + i - 1), (20 + 1, led_pos_inicio + 10 + i + 1), (0, 0, 0), -1)# >,\/    >, \/
            frame = cv2.rectangle(frame, (10, led_pos_inicio + i), (20, led_pos_inicio + 10 + i), (int(b), int(g), int(r)), -1)# >,\/    >, \/

        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit* i
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
