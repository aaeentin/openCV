import cv2

cap = cv2.VideoCapture('sword2.mp4')

i = 159
while (True):
    ret, img = cap.read()
    if (ret == 0): break
    cv2.imwrite(f'dataset2/pic_{i}.png', img)
    i += 1

cap.release()