import cv2

video = cv2.VideoCapture('Cars_and_peds.mp4')

# Pre-trained (haar cascade) human classifier
human_classifier = 'haarcascade_fullbody.xml'

human_tracker = cv2.CascadeClassifier(human_classifier)

while True:
    (read_successful, frame) = video.read()

    if read_successful:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    pedestrians = human_tracker.detectMultiScale(gray_frame)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)

    cv2.imshow('Pedestrian Detector', frame)

    cv2.waitKey(1)

print("code completed")