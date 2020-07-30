### CREATED BY BASHIER DAHMAN ###
### LAST UPDATED 6/2/20 ###
### PLEASE INSTALL ALL MODULES TO BE ABLE TO USE APPLICATION ###


import tkinter
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageFilter
from tkinter import filedialog
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter.colorchooser import *
import time
import cv2 as cv2
import numpy as np

# this creates the main window
top = tkinter.Tk()


#### style of my application ####
style = ThemedStyle(top)
style.set_theme('black')

s = ttk.Style(top)
# s.theme_use('clam')

top.resizable(False, False)

#########################
frame = tkinter.Frame(top)
frame.pack()

# default font name #
font_name = "Calibri"

# user32 = ctypes.windll.user32
# screen_width, screen_height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


#### default font ####
font_path = "C:\Windows\Fonts\calibri.ttf"

# titling the application box 
top.title("Image on Text Editor")
top.geometry("500x500+200+200" )
top.grid()

leftFrame = tkinter.Frame(top)
leftFrame.pack(side=tkinter.LEFT)
rightFrame = tkinter.Frame(top)
rightFrame.pack(side=tkinter.RIGHT)

#################################### QUIT BUTTON #############################################

quit_pane = tkinter.PanedWindow(orient ='vertical') 

quitButton =ttk.Button(top, text ="QUIT", command = top.quit)
quit_pane.add(quitButton)

quit_pane.pack()
quit_pane.place(x = 420, y = 450, height = 30, width = 50)

####################### DEFAULT SHOW COLOR BUTTON #######################

showColor = tkinter.Button(bg = 'gray81')
showColor.pack()
showColor.place(x= 302, y= 174, height = 31, width = 31)

################################### OPEN IMAGE BUTTON AND FUNCTION ########################################

### Function to open files ###
img_window = tkinter.PanedWindow(top, orient='vertical')
def file_opener():
    
    global actual_img
    global original_img
    global filepath

    top.filename = filedialog.askopenfilename(initialdir="*/Images/", title ="Select an Image", filetypes=((".png", "*.png"),(".jpg", "*.jpg")))

    filepath = top.filename

    original_img = Image.open(top.filename)
    
    #################### CLICK LOCATION OF WHERE YOU WANT TO ADD TEXT ####################

    event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))

    imgApp = tkinter.Toplevel()

    # creating an img var of my original image
    img = ImageTk.PhotoImage(original_img)

    #setting up a tkinter canvas with scrollbars
    frame = tkinter.Frame(imgApp, bd=2, relief=tkinter.SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = tkinter.Scrollbar(frame, orient=tkinter.HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=tkinter.E+tkinter.W)
    yscroll = tkinter.Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=tkinter.N+tkinter.S)
    canvas = tkinter.Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set, width = img.width(), height = img.height())
    canvas.grid(row=0, column=0, sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=tkinter.BOTH, expand = 1)

    # adding the image to canvas

    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(cursor = "tcross")
    canvas.config(scrollregion=canvas.bbox(tkinter.ALL))

    # function to be called when mouse is clicked
    def returnCoords(event):
        global cx, cy
        # change the cursor when button is held / click so user knows they selected a coordinate
        canvas.config(cursor = "dotbox")
        cx, cy = event2canvas(event, canvas)
        return cx, cy

    def returnCursor(event):
        canvas.config(cursor = "arrow")
        time.sleep(.7)
        imgApp.destroy()

    # mouseclick event / release
    canvas.bind("<ButtonPress-1>", returnCoords)
    canvas.bind("<ButtonRelease-1>", returnCursor)
    
    imgApp.title("Please select an area on Image")
    imgApp.config(bg="red")
    imgApp.mainloop()


  
# Button to load image #
openImage = tkinter.PanedWindow(orient ='vertical') 

openImageButton = ttk.Button(top, text ="Load Image", command = file_opener)
openImage.add(openImageButton)

loadImgLabel = tkinter.Label(top, text="Step 1: Select an image to edit, then click where to place text:")
loadImgLabel.config(font=('helvetica', 10, "bold"))
loadImgLabel.pack()
loadImgLabel.place(x=50,y=20)

openImage.pack()
openImage.place(x = 50, y = 48, height = 30, width = 250)


################################ FONT SELECTION ######################################
# function for font selection 
def selectedFont(name, index, mode):
    #fontLabel = tkinter.Label(top, text = font_clicked.get()).pack()
    global font_path
    global font_name
    if font_clicked.get() == 'Calibri':
        font_path = "C:\Windows\Fonts\calibri.ttf"
        font_name = 'Calibri'
        return font_name
        return font_path
    elif (font_clicked.get() == 'Comic Sans'):
        font_path = "C:\Windows\Fonts\comic.ttf"
        font_name = 'Comic Sans MS'
        return font_name
        return font_path
    elif (font_clicked.get() == 'Broadway'):
        font_path = "C:\Windows\Fonts\BROADW.ttf"
        font_name = 'Broadway'
        return font_name
        return font_path
    elif (font_clicked.get() == 'STENCIL'):
        font_path = "C:\Windows\Fonts\STENCIL.ttf"
        font_name = 'Stencil'
        return font_name
        return font_path
    elif (font_clicked.get() == 'Blackadder ITC'):
        font_path = "C:\Windows\Fonts\ITCBLKAD.ttf"
        font_name = 'Blackadder ITC'
        return font_name
        return font_path
    elif (font_clicked.get() == 'Magneto'):
        font_path = "C:\Windows\Fonts\MAGNETOB.ttf"
        font_name = 'Magneto'
        return font_name
        return font_path

# options for font selection 

optionsFont = [
    "Calibri",
    "Calibri",
    "Comic Sans",
    "Broadway",
    "STENCIL",
    "Blackadder ITC",
    "Magneto"
]

#### drop down menu ####

font_clicked = tkinter.StringVar()
font_clicked.set(optionsFont[0])


dropDown = ttk.OptionMenu(top, font_clicked, *optionsFont)
dropDown["menu"].config(bg="light pink", fg="black")
# dropDown.config(bg = "gray81")

# setting each font option to have it's corresponding style
dropDown["menu"].entryconfig(0, font=('Calibri', 12))
dropDown["menu"].entryconfig(1, font=('Comic Sans MS', 12))
dropDown["menu"].entryconfig(2, font=('Broadway', 12))
dropDown["menu"].entryconfig(3, font=('Stencil', 12))
dropDown["menu"].entryconfig(4, font=('Blackadder ITC', 12))
dropDown["menu"].entryconfig(5, font=('Magneto', 12))


dropDown.pack()
dropDown.place(x=50,y=108, height = 30, width = 250)

Callbackname = font_clicked.trace_variable('w', selectedFont)

### Menu Label ###
menuLabel= tkinter.Label(top, text="Step 2: Please choose a font from the following menu:")
menuLabel.config(font=('helvetica', 10, "bold"))
menuLabel.pack()
menuLabel.place(x=50,y=85)


######################### COLOR BUTTON AND FUNCTIONS ########################

def _from_rgb(rgb):
    # translates an rgb tuple of int to a tkinter friendly color code
    return "#%02x%02x%02x" % rgb   

def getColor(): 

    global color_result_rgb

    userColor = askcolor()

    rgb_tuple = userColor[0] # gets tuple of RGB values
    color_result_rgb = ', '.join(str(int(x)) for x in rgb_tuple) # setting the tuple, in the correct format 
    rgb_hex = userColor[1]
    showColor.config(bg = rgb_hex)

    return color_result_rgb # return the result 

##### color button #####
colorButton = ttk.Button(text='Select Color', command=getColor)
colorButton.pack()
colorButton.place(x=50,y=175, width = 250, height = 30)


### color Label ###
colorLabel= tkinter.Label(top, text="Step 3: Please choose a font color:")
colorLabel.config(font=('helvetica', 10, "bold"))
colorLabel.pack()
colorLabel.place(x=50,y=149)

#################################### FONT SIZE ComboBox and Function ########################################

fontSizeLabel = tkinter.Label(top, text="Step 4: Please choose a font size (or type custom size):")
fontSizeLabel.config(font=('helvetica', 10, "bold"))
fontSizeLabel.pack()
fontSizeLabel.place(x=50,y=213)

##### OPTIONS FOR FONT SIZE ####
fontSizeOptions = [
    "8",
    "10",
    "12",
    "18",
    "24",
    "32",
    "64",
    "128"
]

### Allows user to type their own font ###
fontSizeClicked = tkinter.StringVar()

fontSizeCombo = ttk.Combobox(top, value = fontSizeOptions, textvariable = fontSizeClicked)
fontSizeCombo.current(0)
# fontSizeCombo.bind("<<ComboboxSelected>>", fontSize)
fontSizeCombo.pack()
fontSizeCombo.place(x=50,y=239, width = 100, height = 25)

################## PHOTO EDITTING MENU AND FUNCTIONS ##########################

####### function for editting the photo ###########
def selectedEdit(event):
    global newImg

    # option for blur effect
    if edit_clicked.get() == 'Blur':
        newImg = original_img.filter(ImageFilter.GaussianBlur(radius = 4))
        return newImg

    # option to flip image 180 degrees
    elif edit_clicked.get() == 'Flip Upside Down':
        newImg = original_img.rotate(180)
        return newImg

    # resize the image by half
    elif edit_clicked.get() == 'Resize Image By Half':
        widthImg, heightImg = original_img.size
        newImg = original_img.resize((int(widthImg / 2), int(heightImg /2)))
        return newImg

    # the emboss effect
    elif edit_clicked.get() == 'Emboss':
        newImg = original_img.filter(ImageFilter.EMBOSS)
        return newImg

    # adding a small colored filter
    elif edit_clicked.get() == 'Color Filter':

        colorFilter = askcolor()
        filter_tuple_new = colorFilter[0] # gets tuple of RGB values

        # get height and width of original img
        widthImg, heightImg = original_img.size

        # set a filter identical in size of original img, and set each pixel to the color of user choose
        filter_img = np.full((heightImg,widthImg,3), filter_tuple_new, np.uint8)

        # recieve img from file
        target_img = cv2.imread(filepath)
        # fuse the images
        fused_image  = cv2.add(target_img,filter_img)

        # set the weights of fused img
        fused_image  = cv2.addWeighted(target_img, 0.8, filter_img, 0.2, 0)
        
        # convert the image back to PIL format
        fused_image = cv2.cvtColor(fused_image, cv2.COLOR_BGR2RGB)
        newImg = Image.fromarray(fused_image)

        return newImg

    # adding a small colored border to the image
    elif edit_clicked.get() == 'Border Effect':
        
        # prompt user for color 
        colorBorder = askcolor()
        border_tuple = colorBorder[0] # gets tuple of RGB values

        # open img in file cv2
        border_img = cv2.imread(filepath)

        # create a border 
        border_img = cv2.copyMakeBorder(border_img, 20,20,20,20, cv2.BORDER_CONSTANT, value=border_tuple)

        # convert the image back to PIL format
        #border_img = cv2.cvtColor(border_img, cv2.COLOR_BGR2RGB)
        newImg = Image.fromarray(border_img)

        return newImg

    # if no option is selected, user just wants to keep the image the way it is
    else:
        newImg = original_img
        return newImg

# options for effect selection 
optionsEdit = [
    "Normal",
    "Normal",
    "Blur",
    "Flip Upside Down",
    "Resize Image By Half",
    "Emboss",
    "Color Filter",
    "Border Effect"
]

#### drop down menu ####

edit_clicked = tkinter.StringVar()
edit_clicked.set(optionsEdit[0])


editDrop = ttk.OptionMenu(top, edit_clicked, *optionsEdit, command=selectedEdit)
editDrop["menu"].config(bg="orange red", fg="black")
# editDrop.config(bg = "gray81")
editDrop.pack()
editDrop.place(x=50,y=287, height = 30, width = 250)

### Menu Label ###
editLabel= tkinter.Label(top, text="Step 5: You can choose to edit your picture:")
editLabel.config(font=('helvetica', 10, "bold"))
editLabel.pack()
editLabel.place(x=50,y=265)



########################################## Text Box ###############################################
# canvas1 = tkinter.Canvas(top, width = 20, height = 150)
# canvas1.pack()
# canvas1.place(x=80, y= 100)

entry1 = ttk.Entry(top,width=30, font=(font_name, 12)) 
entry1.pack()
entry1.place(x=53,y=347)
# canvas1.create_window(100, 140, window=entry1)

entryLabel = tkinter.Label(top, text="Step 6: Type the text to add on image:")
entryLabel.config(font=('helvetica', 10, "bold"))
entryLabel.pack()
entryLabel.place(x=48,y=320)
# canvas1.create_window(100, 110, window=label2)


########################## TEXT TO IMAGE FUNCTION ####################################
def txt_to_img(event=None):
    
    text= entry1.get()
    img_window.destroy()
    draw = ImageDraw.Draw(newImg)

    # did int(float()) incase user input's a float for font size
    font = ImageFont.truetype(font_path, size=int(float(fontSizeClicked.get()))) 

    # starting position of the message
    
    (x, y) = (cx, cy)
    message = text
    color = 'rgb(' + color_result_rgb + ')' # color
    
    # draw the message on the background
    draw.text((x, y), message, fill=color, font=font)

    # (x, y) = (250, 150)
    # name = "Bashier"
    # personFrom = 'From: ' + name
    # color = 'rgb(255, 100, 50)' 
    # draw.text((x, y), personFrom, fill=color, font=font)

    newImg.show()

###### ENTER BUTTON AND IT'S USAGE ######

#Enter Button
enter = tkinter.PanedWindow(orient ='vertical') 

# bind the enter key to basically press "Enter" button
entry1.bind("<Return>", txt_to_img)

enterButton = ttk.Button(top, text ="Enter", command=txt_to_img)
enter.add(enterButton)

enter.pack()
enter.place(x = 308, y = 345, height = 26, width = 60)

##### save as button #####


image_files = [('PNG Files', '*.png*'),  
            ('JPG Files', '*.jpg'), 
            ('All Files', '*.*')] 

def savefile():

    filename = filedialog.asksaveasfile(mode='wb', defaultextension=image_files)
    if not filename:
        return
    newImg.save(filename)

saveAs_button = ttk.Button(top, text = "Save Image As", command = savefile)
saveAs_button.pack()
saveAs_button.place(x = 50, y = 390, height = 30, width = 200)


# main loop of my main application
top.mainloop()
