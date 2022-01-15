# import PIL module
from PIL import Image
import numpy as np
import cv2 as cv
from screeninfo import get_monitors


screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height


def paste_for_screen(filename1,filename):
    # Open Front Image
    frontImage = Image.open(filename)
    # frontImage = frontImage.rotate(180)
    
    # Open Background Image
    background = Image.open(filename1)
    # frontImage = frontImage.resize((int(screen_width),(int(screen_height))))
    
    # resize the front img
    frontImage = frontImage.resize((background.width, background.height), Image.ANTIALIAS)

    # Convert image to RGBA
    frontImage = frontImage.convert("RGBA")
    
    # Convert image to RGBA
    background = background.convert("RGBA")
    
    # Paste the frontImage at (width, height)
    background.paste(frontImage, (0, 0), frontImage)
    
    #converting BRG img fromate  to RGB img fromate which working with cv
    img = np.asarray(background)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
    return img
