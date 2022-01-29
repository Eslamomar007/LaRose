from tkinter import *
import cv2 as cv
from threading import Thread 
from PIL import ImageTk, Image
import keyboard
import numpy as np
from time import strftime ,sleep
from screeninfo import get_monitors
import datetime
from files import create_files
import os
import rotatescreen

# imoport attrabutes
# from logo import chose_logo
from chose_frame import chose_frame
from counter import chose_counter
from img_num import imgnumber
from caption_date import caption_date
# from dis_mode import chose_mode
from second_logo import chose_sec_logo


from paste_two_imges import paste_for_screen
from paste_img_logo import paste_for_logo
from paste_buttons import paste_buttons
from printing import print_photo
from resize_ratio import resize_ratio

vid = cv.VideoCapture(0)
vid.set(3, 1920) # set the resolution
vid.set(4, 1080)
vid.set(cv.CAP_PROP_AUTOFOCUS, 1) # turn the autofocus off




# define screen size
screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height
rotate_screen = rotatescreen.get_primary_display()

def viewing(timer): 
    a = datetime.datetime.now()
    count_number = timer
    x=0
    z = datetime.datetime.now()
    count_color=(0,0,0)
    while True:
        global stop_thread
        global vid
        global captured_img
        _ , img = vid.read()

        b = datetime.datetime.now()
        # img = cv.rotate(img, cv.cv2.ROTATE_180_CLOCKWISE)
        
        captured_img = img
        cv.namedWindow("capturing", cv.WINDOW_NORMAL )
        cv.setWindowProperty("capturing",cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
        # if b-a >= datetime.timedelta(seconds=timer):
        #     stop_thread= False

        if b-a >= datetime.timedelta(seconds=x):
            x+=1
            count_number -=1
            count_color = (0,0,0)

        if b-z >= datetime.timedelta(microseconds=150000):
            count_color= (count_color[0]+20,count_color[1]+20,count_color[2]+20)
            z = datetime.datetime.now()

        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        
        img = img_resizing_screen(img)
        
        # cv.rectangle(img, (0, 0), (screen_width, int(screen_height*.1)), (255, 255,255), thickness=cv.FILLED)
        # img =cv.putText(img, str(count_number), (int(screen_width/3.5), int(screen_height*.17)), 4, 14,count_color, 15, cv.LINE_AA)   
        img =cv.putText(img, str(count_number), (int(screen_width/3.5), int(screen_height*.16)), 2, 14,count_color, 16, cv.LINE_AA)   
        # img =cv.putText(img, str(count_number), (int(screen_width/3), int(screen_height*.8)), 2, 14,count_color, 15, cv.LINE_AA)   
        cv.imshow('capturing', img)
        cv.waitKey(1)

        if  not stop_thread:
            cv.destroyWindow('capturing')
            break                                
        

#modifing image size to screen
def img_resizing_screen(img):
    global w,h
    w,h = resize_ratio(img.shape[0],img.shape[1], width=int(screen_width))
    h = int(h*2)
    w=int(w*.95)
    img = cv.resize(img, (w,h))
    img = cv.copyMakeBorder(img, int((screen_height-h-250)/2), int((screen_height-h-250)/2), 0, 0, cv.BORDER_CONSTANT, value=(255, 255, 255))    
    # # upper border
    # img = cv.rectangle(img, (0, 0), (w, int(screen_height*.1)), (255, 255,255), thickness=cv.FILLED)
    # # lower border
    # img = cv.rectangle(img, (0, int(screen_height*.9)), (screen_width, int(screen_height)), (255, 255,255), thickness=cv.FILLED)
    return img 

# #modifing image size to printer
# def border_printer(img):
#     img = cv.copyMakeBorder(img, int(screen_height*.1), int(screen_height*.1), 0, 0, cv.BORDER_CONSTANT, value=(0, 0, 0))    
#     return img 


#main variables 
keys = ['page up', 'b']


sleepcounter = datetime.datetime.now()
create_files()

frame = chose_frame()
timer = chose_counter()
cap_name, date,color = caption_date()
# logo = chose_logo()
sec_logo = chose_sec_logo()

max_number,max_person = imgnumber()
# display_mode = chose_mode()

logo = 'main_logo'
printer_dir='import/buttons/'+'printer.png'
cam_dir='import/buttons/'+'cam.png'

okay=True
printed_photos = 0
stop_thread = True


while True:
    daytime =strftime("%Y-%m-%d %H_%M_%S")
    day =(datetime.datetime.now()-datetime.timedelta(hours=4)).strftime("%Y-%m-%d") 
    # detecting sleeping mode

    _ , img = vid.read()


    for k in keys:
            sleepcounter = datetime.datetime.now()


    if datetime.timedelta(seconds = 600) + sleepcounter  <= datetime.datetime.now():   
        cv.namedWindow("sleeping", cv.WINDOW_NORMAL )
        cv.setWindowProperty("sleeping",cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
        
        try:       
            for i in os.listdir(day):
                i = cv.imread(day+'/'+i)
                i = cv.resize(i,(int(screen_width), int(screen_height)), Image.ANTIALIAS)           
                cv.imshow('sleeping',i)
                cv.waitKey(3000)
                for k in keys:
                    if keyboard.is_pressed(k):
                        sleepcounter = datetime.datetime.now()
                        cv.destroyWindow('sleeping')
                        break 

        except:
            bg = cv.imread('import/background/back.jpeg')
            bg = cv.resize(bg,(int(screen_width), int(screen_height)), Image.ANTIALIAS)           
            cv.imshow('sleeping',bg)
            cv.waitKey(0)
            sleep(1.5)
            sleepcounter = datetime.datetime.now()
            cv.destroyWindow('sleeping')

        cv.destroyWindow('sleeping')


    if keyboard.is_pressed('b'):
        if timer >0:
            t1 =Thread(target = viewing, args=[timer])
            # t2 = Thread(target=count_down_vid, args=[timer])
            cv.destroyWindow('window')
            t1.start()
            # t2.start()
            sleep(timer)
            stop_thread = False
            t1.join()
            # t2.join()
            
            stop_thread = True

        try:
            img = captured_img
        except:
            pass 


        try:
            os.mkdir(str(day))
        except:
            pass   

        okay = True
        cv.imwrite('photos/'+daytime+'.jpg', img)
        if frame!='None':
            img = paste_for_screen('photos/'+daytime+'.jpg','import/frame/'+frame+'.png')
            cv.imwrite('photos/'+daytime+'.jpg', img)
                    

        # writing on the screen
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

        img = img_resizing_screen(img)
        cv.imwrite(day+'/'+daytime+'.jpg', img)
        
        cv.putText(img, cap_name, (int(screen_width*.01),int(screen_height*.79)), 6, 3,color, 2, cv.LINE_AA)   
        cv.putText(img, date, (int(screen_width*.01),int(screen_height*.85)), 6, 3,color, 2, cv.LINE_AA)   
        to_print = 1
        was_pressed = False
        cv.imwrite('photos/'+daytime+'.jpg', img)
        
        img = paste_buttons('photos/'+daytime+'.jpg',cam_dir, printer_dir) 
        while okay ==True:
            cv.namedWindow("saved", cv.WINDOW_NORMAL )
            cv.setWindowProperty("saved",cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
            cv.imshow('saved', img)
            if keyboard.is_pressed('page up'):
                to_print += 1
                if to_print >max_person:
                    to_print-=1
                sleep(.15)

            if keyboard.is_pressed('page down'):
                if to_print>=2:
                    to_print -= 1
                sleep(.15)
            
            if to_print >= max_person:
                to_print == max_person
            # put text on wihite rectangle
            img = cv.rectangle(img, (int(screen_width*.3), 0), (int(screen_width*.7), int(screen_height*.1)), (255, 255,255), thickness=cv.FILLED)
            cv.putText(img, 'copy: '+str(to_print), (int(screen_width*.33),int(screen_height*.09)), 5, 3,(0, 0, 0), 2, cv.LINE_AA)   
         
            if keyboard.is_pressed('b'):
                # img = cv.rectangle(img, (0, 0), (int(img.shape[0]), int((screen_height-h)/2)), (255, 255,255), thickness=cv.FILLED)
             
                # img = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
                # print_img = cv.rotate(print_img, cv.ROTATE_90_CLOCKWISE)

                print_img = paste_for_logo(day+'/'+daytime+'.jpg','import/buttons/'+logo+'.png')
                cv.imwrite(day+'/'+daytime+'.jpg', print_img)

                if sec_logo !='None':
                    print_img = paste_for_logo(day+'/'+daytime+'.jpg','import/logo/'+sec_logo+'.png','left')
                    cv.imwrite(day+'/'+daytime+'.jpg', print_img)
                    
                text_height = (h*.96) + ((screen_height-h)/2)
                cv.putText(print_img, cap_name, (int(screen_width*.06),int(text_height)), 6, 3,color, 2, cv.LINE_AA)   
                text_height = (h*1.03) + ((screen_height-h)/2)
                # cv.putText(print_img, date, (int(screen_width*.01),int(screen_height*.96)), 6, 2,color, 2, cv.LINE_AA)   
                cv.putText(print_img, date, (int(screen_width*.06),int(text_height)), 6, 2,color, 2, cv.LINE_AA)   

                cv.imwrite(day+'/'+daytime+'.jpg', print_img)
                print_img= cv.imread(day+'/'+daytime+'.jpg')
                h,y,_ = print_img.shape
                print_img = print_img[int(h*.05):h,0:y]
                print_img = print_img[0:int(h*.94),0:y]
                printed_photos+=1
                
                
                
                # w,h = resize_ratio(print_img.shape[0],img.shape[1], width=int(screen_width))
                print_img = cv.resize(print_img, (int(screen_width*.95),int(screen_height*.9)))
                cv.imwrite(day+'/'+daytime+'.jpg', print_img)
                
                for i in range(to_print):
                    try:
                        os.mkdir(str(day))
                    except:
                        pass

                    # if display_mode:
                    #     print_img = cv.rotate(print_img, cv.cv2.ROTATE_90_CLOCKWISE)
                    
                    
                    # print_img = cv.rotate(print_img, cv.ROTATE_90_CLOCKWISE)            

                    # cv.imwrite(day+'/'+daytime+'.jpg', print_img)
                    # print_img= cv.imread(day+'/'+daytime+'.jpg')
                    # h,y,_ = print_img.shape
                    # print_img = print_img[int(h*.15):h,0:y]
                    # print_img = print_img[0:int(h*.7),0:y]
                    # printed_photos+=1
                    
                    
                    
                    # # w,h = resize_ratio(print_img.shape[0],img.shape[1], width=int(screen_width))
                    # print_img = cv.resize(print_img, (int(screen_width*.95),int(screen_height*.9)))

                    cv.imwrite(day+'/'+daytime+'.jpg', print_img)
                    print_photo(day+'/'+daytime+'.jpg')
                    if printed_photos>= max_person:
                        break                    
                okay = False
                os.remove('photos/'+daytime+'.jpg')
                cv.destroyWindow('saved')
            
            if keyboard.is_pressed('w') or keyboard.is_pressed('ctrl+s') or keyboard.is_pressed('s')  :
                os.remove(day+'/'+daytime+'.jpg')
                os.remove('photos/'+daytime+'.jpg')

                okay = False
                cv.destroyWindow('saved')                
            
            cv.waitKey(1)
    cv.namedWindow("window", cv.WINDOW_NORMAL )
    cv.setWindowProperty("window",cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    
    # img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

    # img = cv.rotate(img, cv.cv2.ROTATE_180_CLOCKWISE)
    img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

    try:
        cv.imwrite('i.jpg',img_resizing_screen(img) )
    except:
        _, img = vid.read()
        img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
        cv.imwrite('i.jpg',img_resizing_screen(img) )

    img = paste_buttons('i.jpg',cam_dir, printer_dir)
    cv.imshow('window',img )


    # the 'q' or 'Esc' button is set as the
    if cv.waitKey(1) == ord('q') or keyboard.is_pressed('Q') or keyboard.is_pressed('alt+f4')  or printed_photos>=max_number:
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()

# import cv2
# https://stackoverflow.com/questions/43987467/how-do-i-crop-an-image-in-opencv-and-python-based-on-percentage
# def crop_img(img, scale=1.0):
#     center_x, center_y = img.shape[1] / 2, img.shape[0] / 2
#     width_scaled, height_scaled = img.shape[1] * scale, img.shape[0] * scale
#     left_x, right_x = center_x - width_scaled / 2, center_x + width_scaled / 2
#     top_y, bottom_y = center_y - height_scaled / 2, center_y + height_scaled / 2
#     img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
#     return img_cropped

# img = cv2.imread('lena.jpg')
# img_cropped = crop_img(img, 0.75)
