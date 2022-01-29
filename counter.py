from tkinter import *
import os
from PIL import ImageTk, Image

from screeninfo import get_monitors


def chose_counter():

    # define screen size
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    root = Tk()
    root.title('Chose the counter')
    root.overrideredirect(True)
    root.state('zoomed')

    bg = Image.open('import/background/back.jpeg')
    bg = bg.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)

    # Show image using label
    background = Label( root, image = bg)
    background.place(x = 0,y = 0)

    font=('calibre',15, 'bold')


    label2= Label(root,font=('calibre',20, 'bold'), text='Chose a counter time')
    label2.grid(row=0, column = 0, padx=20,pady=20, sticky='s')
    label3= Label(root,font = ('calibre',1, 'bold'), text='')
    label3.grid(row=1, column = 0,padx=0,pady=int(screen_height*.2),  sticky='s')   
    counter= IntVar()
    def globy():
        global ln
        try: 
            ln= counter.get()
        except:
            ln='None'
    font=('calibre',10, 'bold')
    radiobtn = Radiobutton(root,font=font, variable= counter, text= 'no timer', value =0, command=globy)
    radiobtn.grid(row=2,column=0, padx=20,pady=20, sticky='w')
    radiobtn.select()
    for i in range(5,33,5):
        radiobtn = Radiobutton(root,font=font,text=str(i), variable= counter, value =i, command = globy )
        radiobtn.grid(row=2,column=i+1, padx=20,pady=20, sticky='e')
        
    bt2= Button(root, text="chose, next->", command=root.destroy)
    bt2.grid(row=10, column=0, padx=20,pady=20, sticky ='w')
    bt2.config(font=(('calibre',20, 'bold')))

    root.mainloop()
    try:
        print(ln)
    except:
        chose_counter()
        
    return int(ln)
