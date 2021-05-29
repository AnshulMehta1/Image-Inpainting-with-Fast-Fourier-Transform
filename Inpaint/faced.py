import cv2 as cv


face_classifier=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img= cv.imread("image123.jfif")
gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_classifier.detectMultiScale(gray, 1.1, 3)

for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),4)

cv.imshow("img",img)
cv.waitKey()

