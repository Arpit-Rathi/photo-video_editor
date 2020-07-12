from tkinter import *
from tkinter import filedialog, Canvas
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

# def back(frame1, frame):
#     frame1.pack_forget()
#     frame.pack()

# def new(frame):
#     frame.pack_forget()
#     frame1 = LabelFrame(root, padx=200, pady=280)
#     frame1.pack()
#     background_label = Label(frame, image = background_image)
#     background_label.place(x=0, y=0, relwidth=1, relheight=1)
#     b1 = Button(frame1, text="back", command=lambda:back(frame1,frame))
#     b1.pack()
def dialogbox():
       filename = filedialog.askopenfilename(initialdir="E:\"", title='Select a image file', filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
       if(filename!=''):
         img = cv2.imread(filename)
         cv2.imshow('image', img)
         global int_chosefile
         int_chosefile=1
#def dialogbox2():
 #      filename = filedialog.askopenfilename(initialdir="E:\"", filetypes=(("avi files", "*.mp4")))
def add():
    pass
def neg():
    pass
def blur(canvas3):
    global int_blur
    int_blur=1
    bluradd = Button(canvas3, text="BLUR +",width=6, height=0 ,bd=2, font=bfont2, bg='teal', command=lambda:add()).place(x=350,y=15)
    blurneg = Button(canvas3, text="BLUR -", width=6, height=0, bd=2, font=bfont2, bg='teal', command=lambda:neg()).place(x=350, y=85)
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
       button_save = Button(canvas3, text="SAVE", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=395)
       button_back = Button(canvas3, text="BACK", width=12, height=0, bd=2, font=bfont2, bg='teal').place(x=15,y=465)
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