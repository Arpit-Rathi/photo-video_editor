from tkinter import *
import cv2
root=Tk()
canvas = Canvas(root, width=500, height=600)
canvas.pack()
background = PhotoImage(file = "bg2.png")
button_img = PhotoImage(file = "edit.png").subsample(2,3)
canvas.create_image(250, 300, image=background)
button_edit=Button(root, text='EDIT',width=185, height=50, image=button_img, bg='white', bd=8).place(x=108,y=237)
root.mainloop()