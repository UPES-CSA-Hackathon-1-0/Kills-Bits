import cv2
from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture("video.mp4", )
cap = cv2.VideoCapture(0)

detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ""
        for lm in lmlist:  # lm gives us the landmarks i.e 33 here
            # print(lm)
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
            #              x-axis y-axis  z-axis
            # opencv uses starting points from top left but unity uses from bottom
            # here we need to change y
            with open("Anime.txt", 'w') as f:
                f.writelines(["%s\n" % item for item in posList])
        posList.append(lmString)
    print(len(posList))

    cv2.imshow("VIDEO", img)

    key = cv2.waitKey(1)
    # if key == ord('s'):  # save command
    #     with open("Anime.txt", 'w') as f:
    #         f.writelines(["%s\n" % item for item in posList])
    if key == ord('e'):  # end command
        cv2.imwrite('VIDEO', img)
        cv2.destroyAllWindows()
