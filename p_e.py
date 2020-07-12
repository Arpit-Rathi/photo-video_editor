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
       filename = filedialog.askopenfilename(initialdir="E:\"", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
       img = cv2.imread(filename)
       cv2.imshow('image', img)

def dialogbox2():
       filename = filedialog.askopenfilename(initialdir="E:\"", filetypes=(("avi files", "*.mp4")))

def edit():
    canvas.pack_forget()
    canvas2_image = PhotoImage(file="canvas2.png")
    root.canvas2_image =  canvas2_image
    canvas2= Canvas(root, width=500, height=600)
    canvas2.pack(expand=YES, fill=BOTH)
    canvas2.create_image(250, 300, image=canvas2_image)
    bfont=font.Font(family='Bradley Hand ITC', size=30, weight='bold')
    open_imgb= Button(canvas2, text="Open Images",width=12, height=0 ,bd=2, font=bfont, bg='teal',command=lambda:dialogbox()).place(x=100,y=180)
    open_vidb = Button(canvas2, text="Open Videos", width=12, height=0, bd=2, font=bfont, bg='teal',command=lambda:dialogbox2()).place(x=100,y=300)




button_edit= Button(canvas, text='EDIT', width=185, height=50, image=button_img, bg='white', bd=8, command=edit).place(
    x=108, y=237)

root.mainloop()
cv2.waitKey()
cv2.destroyAllWindows()