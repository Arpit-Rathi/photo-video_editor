from tkinter import *
from tkinter import filedialog, Canvas
from tkinter import messagebox
import tkinter.font as font
import cv2

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
x=2
canvas3 = Canvas(root, width=500, height=600)
int_rot=0
int_blur=0
int_ok=0

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
    global image, blurred,i
    if(int_ok==1):
        image=blurred
        i=blurred

    if(int_ok==2):
        image=i
        blurred=i


def dialogbox():
       filename = filedialog.askopenfilename(initialdir="E:\"", title='Select a image file', filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
       if(filename!=''):
         img = cv2.imread(filename)
         global image,i,blurred
         image=img
         i=img
         blurred=img
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
    global rot_n_c,rot_n_cc,rot_e,flip_y,flip_x,flip_xy
    global l
    global int_blur,int_rot
    int_rot=1
    cv2.imshow('image', image)
    if(int_blur==1):
      bluradd.place_forget()
      blurneg.place_forget()
      l.place_forget()
    rot_n_c.place(x=280,y=45)
    rot_n_cc.place(x=280, y=115)
    rot_e.place(x=280, y=185)
    flip_y.place(x=280, y=255)
    flip_x.place(x=280, y=325)
    flip_xy.place(x=280, y=395)
    ok.place(x=350, y=500)

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
def blur():
    global image
    global int_blur,int_rot
    int_blur=1
    global bluradd
    global rot_n_c,rot_n_cc,rot_e,flip_y,flip_x,flip_xy
    cv2.imshow('image',image)
    bluradd.place(x=350,y=45)
    blurneg.place(x=350, y=115)
    l.place(x=700,y=0)
    ok.place(x=350,y=500)
    if(int_rot==1):
        rot_n_c.place_forget()
        rot_n_cc.place_forget()
        rot_e.place_forget()
        flip_y.place_forget()
        flip_x.place_forget()
        flip_xy.place_forget()








def editoptions(canvas2):
    if(int_chosefile==1):
       canvas2.pack_forget()
       canvas3_image = PhotoImage(file="canvas2.png")
       root.canvas3_image = canvas3_image

       canvas3.pack(expand=YES, fill=BOTH)
       canvas3.create_image(250, 300, image=canvas3_image)
       button_blur=Button(canvas3, text="BLUR",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:blur()).place(x=15,y=45)
       button_filter= Button(canvas3, text="FILTERS", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=115)
       button_draw = Button(canvas3, text="DRAW", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=185)
       button_rotate = Button(canvas3, text="ROTATE", width=12, height=0, bd=2, font=bfont2, bg='teal', command=lambda:rot()).place(x=15,y=255)
       button_brightness = Button(canvas3, text="BRIGHTNESS", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=325)
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
ok = Button(canvas3, text="OK", width=8, height=0, bd=2, font=bfont2, bg='teal', command=lambda:done())

rot_n_c = Button(canvas3, text="90 CLockwise",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(1))
rot_n_cc = Button(canvas3, text="90 Counter",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(2))
rot_e = Button(canvas3, text="180",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(3))
flip_y = Button(canvas3, text="flip vertically",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(4))
flip_x = Button(canvas3, text="flip horizontally",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(5))
flip_xy = Button(canvas3, text="flip both",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:rotate(6))

l=Label()


button_edit= Button(canvas, text='EDIT', width=185, height=50, image=button_img, bg='white', bd=8, command=edit).place(x=108, y=237)
root.mainloop()
cv2.waitKey()
cv2.destroyAllWindows()