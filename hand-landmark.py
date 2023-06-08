import mediapipe as mp
import cv2

mp_drawings = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0) # 0 is setting for webcam

with mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:

# external app download
# read from videocapture
# close

    while(cap.isOpened()):
        ret,frame = cap.read()

        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True

        print(results.multi_hand_landmarks)

        if(results.multi_hand_landmarks):
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawings.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)

        # num 
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        cv2.imshow('video',image)

        if(cv2.waitKey(1)&0xFF == ord('q')):
            break

cap.release()
cv2.destroyAllWindows()