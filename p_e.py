from tkinter import *
import cv2
root=Tk()
root.geometry('600x700')
canvas = Canvas(root, width=600, height=700)
canvas.pack()

background = PhotoImage(file = "bg2.png")
canvas.create_image(600, 700, image=background)

#background_label = Label(root, image=background)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#title=Label(root, text='PHOTO EDITOR', fg='blue')
#title.config(font=("Bradley Hand ITC",30 ))
#title.pack()
button_photo=Button(root, text='EDIT PHOTOS',width=25, height=3)
#background_label.pack()
button_photo.pack()
root.mainloop()