from tkinter import *
import os
from screeninfo import get_monitors
import tkinter.font as font
from tkinter import colorchooser
from PIL import ImageTk, Image

def caption_date():

    # define screen size
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    root = Tk()
    root.title('Caption& Date')
    root.overrideredirect(True)
    root.state('zoomed')

    bg = Image.open('import/background/back.jpeg')
    bg = bg.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)

    # Show image using label
    background = Label( root, image = bg)
    background.place(x = 0,y = 0)
    # Adjust size

    font=('calibre',20, 'bold')
    label1= Label(root,font=font, text='Enter your subtitle').grid(row=0, column = 0,padx=20,pady=20, sticky='w')

    label3= Label(root,font = ('calibre',1, 'bold'), text='')
    label3.grid(row=1, column = 0,padx=20,pady=int(screen_height*.2),  sticky='s')

    
    
    cap_na= StringVar()
    date_var= StringVar()
    def globy():
        global d
        global cn
        cn = caption_name.get()
        d = date.get()
        root.destroy()

    label1= Label(root,font=font, text='Enter caption or name').grid(row=2, column = 0,padx=20,pady=20, sticky='w')
    caption_name = Entry(root,width=30,textvariable = cap_na, font=font)
    caption_name.grid(row=3, column = 0,padx=20,pady=20, sticky='w')

    label2= Label(root,font=font, text='Enter the date').grid(row=2, column = 1,padx=20,pady=20, sticky='w')
    date = Entry(root,width=25, textvariable = date_var, font=font)
    date.grid(row=3, column = 1,padx=20,pady=20, sticky='w')


    date_var.set(' ')
    cap_na.set(' ')
    

    def choose_color():
        # variable to store hexadecimal code of color
        global color
        color_code1 = colorchooser.askcolor(title ="Choose color")
        try:
            color_code = color_code1[0]
            color = (int(color_code[2]),int(color_code[1]),int(color_code[0]))
            caption_name.config(fg=color_code1[1])
            date.config(fg=color_code1[1])  
        except:
            color = (0, 0, 0)
            color_code1 = '#000000'
            caption_name.config(fg=color_code1)
            date.config(fg=color_code1)  
        
 
    
    button = Button(root, text = "Select color",
                command = choose_color)
                
    button.config(font=(('calibre',20, 'bold')))
    button.grid(row=5, column= 0,padx=20,pady=20,sticky='w')

    bt2 = Button(root, text="chose, next->", command=globy)
    bt2.config(font=(('calibre',20, 'bold')))
    bt2.grid(row=10, column=0, padx=20,pady=20, sticky ='w')

    root.mainloop()
    try:
        print(cn, d, color)
    except:
        
        caption_date()
        
    return cn.strip(), d.strip(), color

