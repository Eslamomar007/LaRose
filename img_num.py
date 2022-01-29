from tkinter import *
import os
from screeninfo import get_monitors
from PIL import ImageTk, Image


def imgnumber():

    # define screen size
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    root = Tk()
    root.title('Maximum number of images')
    # root.geometry(str(screen_width) +'x'+ str(screen_height))
    root.overrideredirect(True)
    root.state('zoomed')

    bg = Image.open('import/background/back.jpeg')
    bg = bg.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)

    # Show image using label
    background = Label( root, image = bg)
    background.place(x = 0,y = 0)
    # Adjust size
    font_data=('calibre',15, 'bold')
    label1= Label(root,font=('calibre',20, 'bold'), text='Number of allowed images').grid(row=0, column = 0,padx=20,pady=20, sticky='e')

    def globy():
        global i_number        
        global p_number        
        try:
            i_number =int(numberi.get().strip()) 
            p_number=int(numberp.get().strip()) 
            root.destroy()
        except:
            flush= Label(root,font=font_data, fg = 'red', text='pleas enter only numbers')
            flush.grid(row=4, column = 0,padx=20,pady=20, sticky='w')
            numberi.delete(0,END)
            numberp.delete(0,END)
    
    
    label3= Label(root,font = ('calibre',1, 'bold'), text='')
    label3.grid(row=1, column = 0,padx=0,pady=int(screen_height*.2),  sticky='s')   

    label1= Label(root,font=('calibre',15, 'bold'), text='Enter number of allowed images').grid(row=2, column = 0,padx=20,pady=20, sticky='w')
    numberi = Entry(root,width=10, font=font_data)
    numberi.grid(row=3, column = 0,padx=20,pady=20, sticky='w')
    numberi.insert(END,'1')
    label2= Label(root,font=('calibre',15, 'bold'), text='Enter number of allowed images for person').grid(row=2, column = 2,padx=20,pady=20, sticky='w')
    numberp = Entry(root,width=10, font=font_data)
    numberp.grid(row=3, column = 2,padx=20,pady=20, sticky='w')
    numberp.insert(END,'1')




    bt2= Button(root, text="chose, next->", command=globy)
    bt2.grid(row=10, column=0,padx=20,pady=20, sticky ='w')
    bt2.config(font=(('calibre',20, 'bold')))
    root.mainloop()
    print(i_number,p_number)
    return i_number,p_number
