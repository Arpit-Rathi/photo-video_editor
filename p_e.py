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
int_blur=0
bfont = font.Font(family='Bradley Hand ITC', size=30, weight='bold')
bfont2 = font.Font(family='Bradley Hand ITC', size=20, weight='bold')
imgage = cv2.imread('bg2.png')
x=2



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

def dialogbox():
       filename = filedialog.askopenfilename(initialdir="E:\"", title='Select a image file', filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
       if(filename!=''):
         img = cv2.imread(filename)
         global image
         image=img
         cv2.imshow('image', image)
         global int_chosefile
         int_chosefile=1
#def dialogbox2():
 #      filename = filedialog.askopenfilename(initialdir="E:\"", filetypes=(("avi files", "*.mp4")))
def add(canvas3):
  global x
  global image
  if (x <= 50):


    x=x+1
    l= Label(canvas3, text=x, font=bfont).place(x=400, y=200)

  else:
      messagebox.showwarning("WARNING","Cannot increse blur value above 50")
  blurred = cv2.blur(image, ksize=(x, x))
  cv2.imshow('image', blurred)
  image = blurred

def neg(canvas3):
  global x
  global image
  if(x>1):


    x = x - 1
    l= Label(canvas3, text=x, font=bfont).place(x=400, y=200)

  else:
      messagebox.showwarning("WARNING","Cannot decrease blur value below 1")
  blurred = cv2.blur(image, ksize=(x, x))
  cv2.imshow('image', blurred)
  image = blurred
def blur(canvas3):
    global int_blur
    int_blur=1
    bluradd = Button(canvas3, text="BLUR +",width=8, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:add(canvas3)).place(x=350,y=45)
    blurneg = Button(canvas3, text="BLUR -", width=8, height=0, bd=2, font=bfont2, bg='teal', command=lambda:neg(canvas3)).place(x=350, y=115)
    la = Label(canvas3, text="Keep blur\nvalue\nbetween\n1-50", font=bfont).place(x=320, y=270)
def editoptions(canvas2):
    if(int_chosefile==1):
       canvas2.pack_forget()
       canvas3_image = PhotoImage(file="canvas2.png")
       root.canvas3_image = canvas3_image
       canvas3 = Canvas(root, width=500, height=600)
       canvas3.pack(expand=YES, fill=BOTH)
       canvas3.create_image(250, 300, image=canvas3_image)
       button_blur=Button(canvas3, text="BLUR",width=12, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:blur(canvas3)).place(x=15,y=45)
       button_filter= Button(canvas3, text="FILTERS", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=115)
       button_draw = Button(canvas3, text="DRAW", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=185)
       button_crop = Button(canvas3, text="CROP", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=255)
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



button_edit= Button(canvas, text='EDIT', width=185, height=50, image=button_img, bg='white', bd=8, command=edit).place(x=108, y=237)
root.mainloop()
cv2.waitKey()
cv2.destroyAllWindows()