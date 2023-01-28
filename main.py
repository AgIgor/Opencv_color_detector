import cv2
import time

def start():
    cap = cv2.VideoCapture('full.mp4')
    # cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error opening video stream or file")
    else:
        while cap.isOpened():

            # fps = int(cap.get(5))
            # frame_count = cap.get(7)
            # print("Frame Rate : ", fps, "frames per second"," Frame count : ", frame_count)

            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (1280, 720))
                h, w = frame.shape[:2]

                # time.sleep(.07)

                left = 40
                top = 30

                # circles left
                margin_top = top
                margin_left = left
                for i in range(margin_top, 700, 30):
                    # altura x largura
                    (b, g, r) = (frame[i, margin_left])
                    # largura x altura
                    frame = cv2.circle(frame, (margin_left, i), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                    frame = cv2.circle(frame, (margin_left, i), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)
                    # frame = cv2.line(frame, (margin_left + 25, itens_left), (280, itens_left), (0, 0, 0), thickness=25)
                    # frame = cv2.putText(frame, f'{b}, {g}, {r}', (margin_left + 20, itens_left + 10), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(int(b), int(g), int(r)))

                # circles top
                margin_top = top
                margin_left = left
                for i in range(margin_left, 1250, 30):
                    (b, g, r) = (frame[margin_left, i])
                    frame = cv2.circle(frame, (i, margin_top), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                    frame = cv2.circle(frame, (i, margin_top), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)

                # circles rigth
                margin_top = top
                margin_right = w - left
                for i in range(margin_top, 700, 30):
                    (b, g, r) = (frame[i, margin_right])
                    frame = cv2.circle(frame, (margin_right, i), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                    frame = cv2.circle(frame, (margin_right, i), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)

                # circles botton
                margin_top = h - top
                margin_left = left
                for i in range(margin_left, 1250, 30):
                    (b, g, r) = (frame[margin_top, i])
                    frame = cv2.circle(frame, (i, margin_top), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                    frame = cv2.circle(frame, (i, margin_top), 10, (int(b), int(g), int(r)), thickness=-1, lineType=cv2.LINE_AA)


                cv2.imshow('Frame', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                cap.release()
                start()

cv2.destroyAllWindows()


if __name__ == "__main__":
    start()


