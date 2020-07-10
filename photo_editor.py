from tkinter import *
import cv2
img=cv2.imread('dog.jpg')

x1=5


def open_image():
    img=cv2.imread('dog.jpg')
    cv2.imshow('image', img)

f=0
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 50, (0,0,255), thickness=10)
        cv2.imshow('image', img)
def draw():
    cv2.setMouseCallback('image', click_event)

def blur(x1):
    blurred=cv2.blur(img, ksize=(x1,x1))
    cv2.imshow('image', blurred)
def addblur():
    #if(x>50 or y>50):
        #cv2.putText(img, text='cannot blur more')
    #else:
      global x1
      x1=x1+1
      blur(x1)
def subblur():
    #if(x<0 or y<0):
       # cv2.putText(img, text='This is the limit of decresing blur')
    #else:
      global x1
      x1=x1-1

      blur(x1)


root=Tk()
root.geometry('500x500')
l=Label(root, text='PHOTO EDITOR')
b=Button(root, text='open', command=open_image)
b1=Button(root, text='draw circle', command=draw)
b2=Button(root, text='blur +', command=addblur)
b3=Button(root, text='blur -', command=subblur)

l.pack()
b.pack()
b1.pack()
b2.pack()
b3.pack()

root.mainloop()
cv2.waitKey()
cv2.destroyAllWindows()
