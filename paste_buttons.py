# import PIL module
from screeninfo import get_monitors
from PIL import Image
import numpy as np
import cv2 as cv

# screen dimintions
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
unite = int(screen_height*.1)

def paste_buttons(back,front_left=None,front_right=None,front_midel =None):

    background = Image.open(back)
    background = background.convert("RGBA")

    if front_left :
        position = (0, 0)
        frontImage = Image.open(front_left)
        frontImage = frontImage.resize((int(unite*1.5), unite), Image.ANTIALIAS)
        frontImage = frontImage.convert("RGBA")
        background.paste(frontImage, position, frontImage)
       
    if front_right :
        frontImage2 = Image.open(front_right)
        frontImage2 = frontImage2.resize((int(unite*1.5), unite), Image.ANTIALIAS)
        frontImage2 = frontImage2.convert("RGBA")
        position = (int((background.width*.99)-(frontImage2.width)), int(0))
        background.paste(frontImage2, position, frontImage2)
        
    if front_midel  :
        frontImage3 = Image.open(front_midel )        
        frontImage3 = frontImage3.resize((int(unite*1.5), unite), Image.ANTIALIAS)
        frontImage3 = frontImage3.convert("RGBA")
        position = (int((background.width*.99)-(frontImage3.width)), int(0))
        background.paste(frontImage3, position, frontImage3)
                      
    #converting BRG img fromate  to RGB img fromate which working with cv
    img = np.asarray(background)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
    
    return img

