from tkinter import *
import os
from screeninfo import get_monitors
from PIL import ImageTk, Image


def chose_frame():

    # define screen size
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    root = Tk()
    root.title('Frames')
    root.state('zoomed')
    root.overrideredirect(True)

    bg = Image.open('import/background/back.jpeg')
    bg = bg.resize((screen_width, screen_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)

    # Show image using label
    background = Label( root, image = bg)
    background.place(x = 0,y = 0)
    # Adjust size

   
    font=('calibre',20, 'bold')

    imgs = os.listdir('import/frame/')
    label2= Label(root,font = font, text='Chose a Frame')
    label2.grid(row=0, column = 0,padx=20,pady=20,  sticky='s')
    label3= Label(root,font = font, text='')
    label3.grid(row=1, column = 0,padx=20,pady=int(screen_height*.2),  sticky='s')
    co_number=2
    ro_number=2
   
    frame_name = StringVar()
    def globy():
        global fn
        try: 
            fn= frame_name.get()
        except:
            fn=None

    radiobtn = Radiobutton(root,font=('calibre',20, 'bold'), variable= frame_name, text= 'no frame', value ='None', command=globy)
    radiobtn.grid(row=2,column=0,padx=20,pady=20, sticky='w')
    
    for i, name in enumerate(imgs):
        global  img
        img = Image.open('import/frame/'+name)
        width, height = img.size
        new_height = int(screen_height*.15)
        new_width = int(screen_width*.15)
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        if i%2==0:
            co_number +=1
            ro_number=2
            
        imgs[i]= img
        radiobtn = Radiobutton(root, variable= frame_name, image=img, value =name[:-4], command = globy )
        radiobtn.grid(row=ro_number, column=co_number,padx=20, pady=20, sticky='e')
        ro_number+=1



    bt2 = Button(root, text="chose, next->", command=root.destroy)
    bt2.grid(row=10, column=0,padx=20,pady=20, sticky ='s')
    bt2.config(font=(('calibre',20, 'bold')))    
    root.mainloop()

    try:
        print(fn)
    except:
        chose_frame()
        
    return fn
