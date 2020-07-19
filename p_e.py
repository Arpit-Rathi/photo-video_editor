from tkinter import *
from tkinter import filedialog, Canvas
from tkinter import messagebox
import tkinter.font as font
import cv2
import numpy as np

root = Tk()
canvas = Canvas(root, width=500, height=600)
canvas.pack()
background = PhotoImage(file="bg2.png")
button_img = PhotoImage(file="edit.png").subsample(2, 3)
canvas.create_image(250, 300, image=background)
int_chosefile=0
bfont = font.Font(family='Bradley Hand ITC', size=30, weight='bold')
bfont2 = font.Font(family='Bradley Hand ITC', size=20, weight='bold')
image = cv2.imread('bg2.png')
i = cv2.imread('bg2.png')
blurred = cv2.imread('bg2.png')
bright= cv2.imread('bg2.png')
fil= cv2.imread('bg2.png')
x=2
x1=0
x2=0
canvas3 = Canvas(root, width=500, height=600)
int_rot=0
int_blur=0
int_ok=0
int_bright=0
int_filt=0

def back(canvas3,canvas2):
      canvas3.pack_forget()
      canvas2.pack()
def save(entry,root2):
    image_loc = "E:\Computer_Vision\photo_editor\saved_images\\" + entry.get() + ".jpg"
    cv2.imwrite(image_loc, image)
    root2.destroy()
def writename():
    root2 = Tk()
    label=Label(root2, text='Enter name of the file to be saved ')
    entry=Entry(root2, width=50, borderwidth=10)
    button=Button(root2, text="Save", width=10, height=0, bd=2,command=lambda:save(entry,root2))
    label.pack()
    entry.pack()
    button.pack()
    root2.mainloop()
def done():
    global int_ok
    global image, blurred,i,bright,fil
    if(int_ok==1):
        image=blurred
        i=blurred
        bright=blurred
        fil=blurred
    if(int_ok==2):
        image=i
        blurred=i
        bright=i
        fil=i
    if(int_ok==3):
        image= bright
        i=bright
        blurred=bright
        fil=bright
    if(int_ok==4):
        image=fil
        i=fil
        blurred=fil
        bright=fil
        



def dialogbox():
       filename = filedialog.askopenfilename(initialdir="E:\"", title='Select a image file', filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
       if(filename!=''):
         img = cv2.imread(filename)
         global image,i,blurred,bright,fil
         image=img
         i=img
         blurred=img
         bright=img
         fil=img
         cv2.imshow('image', image)
         global int_chosefile
         int_chosefile=1
#def dialogbox2():
 #      filename = filedialog.askopenfilename(initialdir="E:\"", filetypes=(("avi files", "*.mp4")))
def rotate(x):
    global int_ok
    global image,i

    if(x==1):
        i= cv2.rotate(i, cv2.ROTATE_90_CLOCKWISE)
    if (x == 2):
        i = cv2.rotate(i, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if (x == 3):
        i = cv2.rotate(i, cv2.ROTATE_180)
    if (x == 4):
        i = cv2.flip(i, 0)
    if (x == 5):
        i = cv2.flip(i, 1)
    if (x == 6):
        i = cv2.flip(i, -1)

    cv2.imshow('image', i)
    int_ok=2
def rot():
    global image
    global bluradd
    global blurneg
    global briadd,brineg,ok
    global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21
    global rot_n_c,rot_n_cc,rot_e,flip_y,flip_x,flip_xy
    global l,l1
    global int_blur,int_rot,int_bright,x,x1,x2,int_filt
    x=0
    x1=0
    x2=0
    int_rot=1
    cv2.imshow('image', image)
    if(int_blur==1):
      bluradd.place_forget()
      blurneg.place_forget()
      l.place_forget()
      int_blur=0
      ok.place_forget()
    if(int_bright==1):
        briadd.place_forget()
        brineg.place_forget()
        l1.place_forget()
        int_bright=0
        ok.place_forget()
    if (int_filt == 1):
        f1.place_forget()
        f2.place_forget()
        f3.place_forget()
        f4.place_forget()
        f5.place_forget()
        f6.place_forget()
        f7.place_forget()
        f8.place_forget()
        f9.place_forget()
        f10.place_forget()
        f11.place_forget()
        f12.place_forget()
        f13.place_forget()
        f14.place_forget()
        f15.place_forget()
        f16.place_forget()
        f17.place_forget()
        f18.place_forget()
        f19.place_forget()
        f20.place_forget()
        f21.place_forget()
        ok.place_forget()
        int_filt = 0

    rot_n_c.place(x=280,y=45)
    rot_n_cc.place(x=280, y=115)
    rot_e.place(x=280, y=185)
    flip_y.place(x=280, y=255)
    flip_x.place(x=280, y=325)
    flip_xy.place(x=280, y=395)
    ok.place(x=350, y=500)

def filt(x):
    global fil,image
    global int_ok
    fil=image
    int_ok=4
    if(x==1):
        fil= cv2.cvtColor(fil, cv2.COLOR_BGR2GRAY)
    if (x == 2):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2RGB)
    if (x == 3):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2HSV)
    if (x == 4):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2HLS)
    if (x == 5):
        fil=cv2.Sobel(fil,cv2.CV_64F,1,0,ksize=11)
    if (x == 6):
        fil = cv2.Sobel(fil, cv2.CV_64F, 0, 1, ksize=11)
    if (x == 7):
        fil= cv2.cvtColor(fil, cv2.COLOR_BGR2LUV)
    if (x == 8):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2XYZ)
    if (x == 9):
        xx = cv2.Sobel(fil, cv2.CV_64F, 1, 0, ksize=11)
        yy = cv2.Sobel(fil, cv2.CV_64F, 0, 1, ksize=11)
        fil=cv2.addWeighted(xx,0.5,yy,0.5,0)
    if (x == 10):
         fil = cv2.cvtColor(fil, cv2.COLOR_BGR2LAB)
    if (x == 11):
         fil = cv2.cvtColor(fil, cv2.COLOR_BGR2YUV)
    if (x == 12):
        k=np.ones((5,5), dtype=np.uint8)
        fil=cv2.erode(fil,k,5)
    if (x == 13):
        k = np.ones((5, 5), dtype=np.uint8)
        fil = cv2.dilate(fil, k, 5)
    if (x == 14):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2HLS_FULL)
    if (x == 15):
        fil = np.asarray(cv2.cvtColor(fil, cv2.COLOR_BGR2GRAY))-50
    if (x == 16):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2YCR_CB)
    if (x == 17):
        fil = np.asarray(cv2.cvtColor(fil, cv2.COLOR_BGR2GRAY))+80
    if (x == 18):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2Luv)
    if (x == 19):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2BGRA)
    if (x == 20):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2HSV_FULL)
    if (x == 21):
        fil = cv2.cvtColor(fil, cv2.COLOR_BGR2YCrCb)
    cv2.imshow('image', fil)

def add():
  global int_ok
  global x
  global image
  global l
  global blurred
  if (x <= 50):
    x=x+1
    l.place_forget()
    l= Label(canvas3, text=x, font=bfont)
    l.place(x=400, y=200)
  else:
      messagebox.showwarning("WARNING","Cannot increse blur value above 50")
  blurred = cv2.blur(image, ksize=(x, x))
  cv2.imshow('image', blurred)
  int_ok=1

def neg():
  global x,int_ok
  global image,blurred
  global l
  if(x>1):
    x = x - 1
    l.place_forget()
    l= Label(canvas3, text=x, font=bfont)
    l.place(x=400, y=200)
  else:
      messagebox.showwarning("WARNING","Cannot decrease blur value below 1")
  blurred = cv2.blur(image, ksize=(x, x))
  cv2.imshow('image', blurred)
  int_ok=1

def addb():
  global int_ok
  global x1,x2
  global image
  global l1
  global bright
  if (x1 <= 100):
    x1=x1+1
    l1.place_forget()
    l1= Label(canvas3, text=x1, font=bfont)
    l1.place(x=400, y=200)
  else:
      messagebox.showwarning("WARNING","Cannot increse brightness value above 100")

  bright = np.asarray(image)
  bright = np.where((bright + x1) < bright, 255, (bright + x1))
  cv2.imshow('image', bright)
  int_ok=3
  x2=0

def negb():
  global int_ok
  global x2,x1
  global image
  global l1
  global bright
  if (x2 <= 100):
    x2=x2+1
    l1.place_forget()
    l1= Label(canvas3, text=x2, font=bfont)
    l1.place(x=400, y=200)
  else:
      messagebox.showwarning("WARNING","Cannot decrease brightness value below 100")

  bright = np.asarray(image)
  bright = np.where((bright - x2) > bright, 0 , (bright - x2))

  cv2.imshow('image', bright)
  int_ok=3
  x1=0


def blur():
    global image
    global int_blur,int_rot,int_bright,x1,x2,int_filt
    int_blur=1
    global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21
    global bluradd,blurneg
    global rot_n_c,rot_n_cc,rot_e,flip_y,flip_x,flip_xy
    global briadd,brineg
    global l1
    cv2.imshow('image', image)
    x1=0
    x2=0
    if (int_rot == 1):
        rot_n_c.place_forget()
        rot_n_cc.place_forget()
        rot_e.place_forget()
        flip_y.place_forget()
        flip_x.place_forget()
        flip_xy.place_forget()
        ok.place_forget()
        int_rot=0
    if(int_bright==1):
        briadd.place_forget()
        brineg.place_forget()
        ok.place_forget()
        int_bright=0
        l1.place_forget()
    if (int_filt == 1):
        f1.place_forget()
        f2.place_forget()
        f3.place_forget()
        f4.place_forget()
        f5.place_forget()
        f6.place_forget()
        f7.place_forget()
        f8.place_forget()
        f9.place_forget()
        f10.place_forget()
        f11.place_forget()
        f12.place_forget()
        f13.place_forget()
        f14.place_forget()
        f15.place_forget()
        f16.place_forget()
        f17.place_forget()
        f18.place_forget()
        f19.place_forget()
        f20.place_forget()
        f21.place_forget()
        ok.place_forget()
        int_filt = 0

    bluradd.place(x=350,y=45)
    blurneg.place(x=350, y=115)
    l.place(x=700,y=0)
    ok.place(x=350,y=500)

def brit():
    global image
    global int_blur, int_rot, int_bright,int_filt
    int_bright = 1
    global bluradd, blurneg
    global rot_n_c, rot_n_cc, rot_e, flip_y, flip_x, flip_xy
    global briadd, brineg
    global f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21
    global l,l1,x
    x=0
    cv2.imshow('image', image)
    if (int_rot == 1):
        rot_n_c.place_forget()
        rot_n_cc.place_forget()
        rot_e.place_forget()
        flip_y.place_forget()
        flip_x.place_forget()
        flip_xy.place_forget()
        ok.place_forget()
        int_rot = 0
    if (int_blur == 1):
        bluradd.place_forget()
        blurneg.place_forget()
        ok.place_forget()
        int_blur = 0
        l.place_forget()
    if(int_filt==1):
        f1.place_forget()
        f2.place_forget()
        f3.place_forget()
        f4.place_forget()
        f5.place_forget()
        f6.place_forget()
        f7.place_forget()
        f8.place_forget()
        f9.place_forget()
        f10.place_forget()
        f11.place_forget()
        f12.place_forget()
        f13.place_forget()
        f14.place_forget()
        f15.place_forget()
        f16.place_forget()
        f17.place_forget()
        f18.place_forget()
        f19.place_forget()
        f20.place_forget()
        f21.place_forget()
        ok.place_forget()
        int_filt=0

    briadd.place(x=270, y=45)
    brineg.place(x=270, y=115)
    l1.place(x=700, y=0)
    ok.place(x=350, y=500)

def filter():
    global image
    global int_blur, int_rot, int_bright, int_filt
    int_filt = 1
    global f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21
    global bluradd, blurneg
    global rot_n_c, rot_n_cc, rot_e, flip_y, flip_x, flip_xy
    global briadd, brineg
    global l, l1, x,x1,x2
    x = 0
    x1=0
    x2=0
    cv2.imshow('image', image)
    if (int_rot == 1):
        rot_n_c.place_forget()
        rot_n_cc.place_forget()
        rot_e.place_forget()
        flip_y.place_forget()
        flip_x.place_forget()
        flip_xy.place_forget()
        ok.place_forget()
        int_rot = 0
    if (int_blur == 1):
        bluradd.place_forget()
        blurneg.place_forget()
        ok.place_forget()
        int_blur = 0
        l.place_forget()
    if (int_bright == 1):
        briadd.place_forget()
        brineg.place_forget()
        ok.place_forget()
        int_bright = 0
        l1.place_forget()

    f1.place(x=270,y=45)
    f2.place(x=350, y=45)
    f3.place(x=430, y=45)
    f4.place(x=270, y=115)
    f5.place(x=350, y=115)
    f6.place(x=430, y=115)
    f7.place(x=270, y=185)
    f8.place(x=350, y=185)
    f9.place(x=430, y=185)
    f10.place(x=270, y=255)
    f11.place(x=350, y=255)
    f12.place(x=430, y=255)
    f13.place(x=270, y=335)
    f14.place(x=350, y=335)
    f15.place(x=430, y=335)
    f16.place(x=270, y=405)
    f17.place(x=350, y=405)
    f18.place(x=430, y=405)
    f19.place(x=270, y=475)
    f20.place(x=350, y=475)
    f21.place(x=430, y=475)
    ok.place(x=350, y=540)



def editoptions(canvas2):
    if(int_chosefile==1):
       canvas2.pack_forget()
       canvas3_image = PhotoImage(file="canvas2.png")
       root.canvas3_image = canvas3_image

       canvas3.pack(expand=YES, fill=BOTH)
       canvas3.create_image(250, 300, image=canvas3_image)
       button_blur=Button(canvas3, text="BLUR",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:blur()).place(x=15,y=45)
       button_filter= Button(canvas3, text="FILTERS", width=12, height=0, bd=2, font=bfont2, bg='teal', command=lambda:filter()).place(x=15,y=115)
       button_draw = Button(canvas3, text="DRAW", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=185)
       button_rotate = Button(canvas3, text="ROTATE", width=12, height=0, bd=2, font=bfont2, bg='teal', command=lambda:rot()).place(x=15,y=255)
       button_brightness = Button(canvas3, text="BRIGHTNESS", width=12, height=0, bd=2, font=bfont2, bg='teal', command=lambda:brit()).place(x=15,y=325)
       button_save = Button(canvas3, text="SAVE", width=12, height=0, bd=2, font=bfont2, bg='teal',command=lambda:writename()).place(x=15,y=395)
       button_back = Button(canvas3, text="BACK", width=12, height=0, bd=2, font=bfont2, bg='teal',command=lambda:back(canvas3,canvas2)).place(x=15,y=465)
def edit():
    canvas.pack_forget()
    canvas2_image = PhotoImage(file="canvas2.png")
    root.canvas2_image =  canvas2_image
    canvas2= Canvas(root, width=500, height=600)
    canvas2.pack(expand=YES, fill=BOTH)
    canvas2.create_image(250, 300, image=canvas2_image)

    open_imgb= Button(canvas2, text="Open Images",width=12, height=0 ,bd=2, font=bfont, bg='teal',command=lambda:dialogbox()).place(x=100,y=150)
    open_vidb = Button(canvas2, text="Open Videos", width=12, height=0, bd=2, font=bfont, bg='teal',command=lambda:dialogbox2()).place(x=100,y=270)
    editfile = Button(canvas2, text="EDIT", width=6, height=0, bd=2, font=bfont2, bg='teal',command=lambda:editoptions(canvas2)).place(x=190, y=390)

bluradd = Button(canvas3, text="BLUR +",width=8, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:add())
blurneg = Button(canvas3, text="BLUR -", width=8, height=0, bd=2, font=bfont2, bg='teal', command=lambda:neg())

briadd= Button(canvas3, text="BRIGHTNESS +",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:addb())
brineg= Button(canvas3, text="BRIGHTNESS -",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:negb())

ok = Button(canvas3, text="OK", width=8, height=0, bd=2, font=bfont2, bg='teal', command=lambda:done())

rot_n_c = Button(canvas3, text="90 CLockwise",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(1))
rot_n_cc = Button(canvas3, text="90 Counter",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(2))
rot_e = Button(canvas3, text="180",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(3))
flip_y = Button(canvas3, text="flip vertically",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(4))
flip_x = Button(canvas3, text="flip horizontally",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(5))
flip_xy = Button(canvas3, text="flip both",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(6))

f1= Button(canvas3, text="1",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(1))
f2= Button(canvas3, text="2",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(2))
f3= Button(canvas3, text="3",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(3))
f4= Button(canvas3, text="4",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(4))
f5= Button(canvas3, text="5",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(5))
f6= Button(canvas3, text="6",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(6))
f7= Button(canvas3, text="7",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(7))
f8= Button(canvas3, text="8",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(8))
f9= Button(canvas3, text="9",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(9))
f10= Button(canvas3, text="10",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(10))
f11= Button(canvas3, text="11",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(11))
f12= Button(canvas3, text="12",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(12))
f13= Button(canvas3, text="13",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(13))
f14= Button(canvas3, text="14",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(14))
f15= Button(canvas3, text="15",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(15))
f16= Button(canvas3, text="16",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(16))
f17= Button(canvas3, text="17",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(17))
f18= Button(canvas3, text="18",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(18))
f19= Button(canvas3, text="19",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(19))
f20= Button(canvas3, text="20",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(20))
f21= Button(canvas3, text="21",width=3, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:filt(21))

l=Label()
l1=Label()

button_edit= Button(canvas, text='EDIT', width=185, height=50, image=button_img, bg='white', bd=8, command=edit).place(x=108, y=237)
root.mainloop()
cv2.waitKey()
cv2.destroyAllWindows()