from tkinter import *
import os
from screeninfo import get_monitors
from PIL import ImageTk, Image


def chose_sec_logo():

    # define screen size
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    root = Tk()
    root.title('Second Logo')
    root.geometry(str(screen_width) +'x'+ str(screen_height))
    root.overrideredirect(True)
    root.state('zoomed')

    bg = Image.open('import/background/back.jpeg')
    bg = bg.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)

    # Show image using label
    background = Label( root, image = bg)
    background.place(x = 0,y = 0)
    font = ('calibre',20, 'bold')


    imgs = os.listdir('import/logo/')
    Label2= Label(root,font=('calibre',20, 'bold'), text='Chose The Second Logo').grid(row=0, column = 0, padx=20,pady=20, sticky='s')
    label3= Label(root,font = font, text='')
    label3.grid(row=1, column = 0,padx=20,pady=int(screen_height*.2),  sticky='s')

    co_number=2
    ro_number=2
    logo_name = StringVar()
    def globy():
        global ln
        try: 
            ln= logo_name.get()
        except:
            ln='None'

    radiobtn = Radiobutton(root, variable= logo_name,font=('calibre',15, 'bold'), text= 'no logo', value ='None', command=globy).grid(row=9,column=0, padx=20,pady=20, sticky='w')
    
    for i, name in enumerate(imgs):
        img = Image.open('import/logo/'+name)
        width, height = img.size
        new_height = int(screen_height*.1)
        new_width = int(screen_width*.3)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        if i%3==0:
            co_number +=1
            ro_number=2

        imgs[i]= img
        radiobtn = Radiobutton(root,variable= logo_name, image=img, value =name[:-4], command = globy ).grid(row=ro_number,column=co_number, padx=10,pady=10, sticky='e')
        ro_number+=1
    bt2= Button(root, text="chose, next->", command=root.destroy)
    bt2.grid(row=10, column=0, padx=20,pady=20, sticky ='w')
    bt2.config(font=(('calibre',20, 'bold')))    
    
    root.mainloop()
    try:
        print(ln)
    except:
        chose_sec_logo()
        
    return ln
