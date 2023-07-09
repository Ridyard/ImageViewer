
#codemy - image viewer app

from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
import os

root = Tk()
root.title('Image Viewer')
root.iconbitmap(r'C:\Users\alexa\Documents\Workspace\Python\Projects - small\Image Viewer\photocameraoutline_80020.ico')

# declare widgets
# image items
my_pics = Path(r'C:\Users\alexa\Documents\Workspace\Python\Projects - small\Image Viewer\Images')
image_list = []

for k,v in enumerate(os.listdir(my_pics)):
    my_img = ImageTk.PhotoImage(Image.open(Path(my_pics/v))) # use this line (image.open() to use jpg and png with tkinter
    image_list.append(my_img)

my_label = Label(image=image_list[0]) # assign the first image as the initial / default image on the img viewer app



def forward(my_label, button_forward, button_back, image_num):
    my_label.grid_forget() # clear the outgoing image
    
    my_label = Label(image=image_list[image_num-1])#image in list is dictated by the parameter passed in, ie the 'image_num+1' or 'image_num-1' below  
    button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, image_num+1))
    button_back = Button(root, text="<", command=lambda: back(my_label, button_forward, button_back, image_num-1))
    
    if image_num == 3:
        button_forward = Button(root, text=">", state=DISABLED)


    # re-put the widgets on the screen with every button press / screen update
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back(my_label, button_forward, button_back, image_num):
    my_label.grid_forget() # clear the outgoing image
    
    my_label = Label(image=image_list[image_num-1])#image in list is dictated by the parameter passed in, ie the 'image_num+1' or 'image_num-1' below  
    button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, image_num+1))
    button_back = Button(root, text="<", command=lambda: back(my_label, button_forward, button_back, image_num-1))
    
    if image_num == 1:
        button_back = Button(root, text="<", state=DISABLED)
        
    # re-put the widgets on the screen with every button press / screen update
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


#button items
button_forward = Button(root, text=">", command=lambda: forward(my_label, button_forward, button_back, 2))#lambda to pass something through a button command
button_back = Button(root, text="<", state=DISABLED)


# add widgets to root
my_label.grid(row=0, column=0, columnspan=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

root.mainloop()


