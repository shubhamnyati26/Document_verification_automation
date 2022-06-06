import cv2
def Img_Face(s):
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  img = cv2.imread(s)
  flag1=0
  faces = face_cascade.detectMultiScale(img, 1.1, 4)
  for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    flag1=1
  return(flag1)


def Img_Sign(s):
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  img = cv2.imread(s)
  flag=1
  faces = face_cascade.detectMultiScale(img, 1.1, 4)
  for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    flag=0
  return(flag)


#Img("C:\\Users\\Subham Kumar Sharma\\Desktop\\test.jpg")
