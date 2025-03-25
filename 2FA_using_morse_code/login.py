import cv2
import datetime
import pandas as pd
import time

from tkinter import *

from playsound import playsound

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
df=pd.read_csv("UserDetails.csv")
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0
var2=0
var=0
t=0
var1=0
def successful():
    root=Tk()
    root.geometry('250x150')
    root.title("Success")
    lbl=Label(root, text="Logged In Successfully")
    print("Login Successful1111")   
    lbl.pack()

    root.mainloop()

def unsuccessful():
    root=Tk()
    root.geometry('150x50')
    root.title("UnSuccess")
    lbl=Label(root, text="Logged In UnSuccessful")
    print("Login unSuccessful")
    lbl.pack()
    root.mainloop()

while True:
    now = datetime.datetime.now()
    ret, im =cam.read()
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    if t==1:
        t=0
        break
    
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        Id,i = recognizer.predict(gray[y:y+h,x:x+w])

        print(i)  ##successful
        if i < 55:
            aa=df.loc[df['Id'] == Id]['name'].values
            tt=str(Id)+"-"+aa
            Id = df.loc[df['Id']== Id] ['name'].values
            var1=1
        else:
            count=count+1
            Id = "unknown"
            if count > 10:
                count=0
            Id="unknown"
            print("unknown")
            cv2.imwrite("frame.png",im)
            print("mail Sent")
            playsound("2.mp3")
            time.sleep(5)
            mon=0
            var2=1
                      

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

    cv2.imshow('im',im)
    
    if var2==1 and count > 5:
        var2=0
        print("unsuccess")
        unsuccessful()
        t=1
        cam.release()
        cv2.destroyAllWindows()
        break

    elif var1==1:
        var1=0
        print("Success")
        successful()
        t=1
        cam.release()
        cv2.destroyAllWindows()
        break

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()