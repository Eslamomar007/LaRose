# import PIL module
from PIL import Image
import numpy as np
import cv2 as cv


def paste_for_logo(filename1,filename, l = None):

    # Open Front Image
    frontImage = Image.open(filename)
    
    # Open Background Image
    background = Image.open(filename1)
    
    # resize the front img
    unite = int(background.width)*1.5
    frontImage = frontImage.resize((int(unite/4), int(unite/6)), Image.ANTIALIAS)

    # Convert image to RGBA
    frontImage = frontImage.convert("RGBA")
    
    # Convert image to RGBA
    background = background.convert("RGBA")
    position=(int((background.width/2)-(frontImage.width/2)), int(frontImage.height)-140)
    
    if l=='left':
        position=(int(background.width-frontImage.width)-int(background.width*.05),int(background.height-frontImage.height)-50)

    # Paste the frontImage at (width, height)
    background.paste(frontImage, position, frontImage)
    
    #converting BRG img fromate  to RGB img fromate which working with cv
    img = np.asarray(background)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
    
    return img
