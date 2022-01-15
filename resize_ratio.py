import cv2 as cv
def resize_ratio(w,h, width=None, height=None):
    dim = None
    if width is None and height is None:
        return w,h
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return dim


# image = cv2.imread('img.png')
# resize = ResizeWithAspectRatio(image, width=1280) # Resize by width OR
# resize = ResizeWithAspectRatio(image, height=1280) # Resize by height 
