import cv2
import time

def start():
    # cap = cv2.VideoCapture('colors.png')
    cap = cv2.VideoCapture('hd.mp4')
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

                altura_inicial = 30
                larg_pos_inicio = 10
                for i in range(altura_inicial, 700, 30):
                    # altura x largura
                    (b, g, r) = (frame[i, larg_pos_inicio])
                    # largura x altura
                    frame = cv2.circle(frame, (larg_pos_inicio, i), 12, (0, 0, 0), thickness=-1, lineType=cv2.LINE_AA)
                    frame = cv2.circle(frame, (larg_pos_inicio, i), 10, (int(b), int(g), int(r)), thickness=-1,lineType=cv2.LINE_AA)

                    frame = cv2.line(frame, (larg_pos_inicio + 25, i), (280, i), (0, 0, 0), thickness=25)
                    frame = cv2.putText(frame, f'{b}, {g}, {r}', (larg_pos_inicio + 20, i + 10), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(int(b), int(g), int(r)))
                    cv2.imshow('Frame', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                cap.release()
                start()

cv2.destroyAllWindows()


if __name__ == "__main__":
    start()


