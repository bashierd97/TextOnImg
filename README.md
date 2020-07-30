# TextOnImg
## This is a python GUI application (Windows), allowing you to write text on an image with a select amount of fonts / effects. You can view your editted image prior to saving it. One of my first personal programs, just wanted to be able to create an application for creating logos / editting images in a few simple steps. You can easily add / remove fonts to your likings, and create effects as well.

### Instructions
- Install necessary modules using ```pip install -r requirements.txt``` on your command prompt
- Run the script using ```python Txt-On-Img.py```

### Adding New Fonts
In the font selection part of the code, there'll be several options for all the fonts. If you have a Windows machine, all font paths will usually be in the same place, if not you can update it to wherever all the fonts are located on your machine. Now you can either replace, or add in another font selection following this format:

- Let's say we wanted to replace the Comic Sans font (the audacity right?) 
```python
    elif (font_clicked.get() == 'Comic Sans'):
        font_path = "C:\Windows\Fonts\comic.ttf"
        font_name = 'Comic Sans MS'
        return font_name
        return font_path
```
In this section we would replace 'Comic Sans' inside the condition statement, with whatever new font name we will be choosing. In this example, we will be choosing the font 'Gigi'. We also then replace the path of the Comic Sans font, with the Gigi font path. On my machine this results in "C:\Windows\Fonts\GIGI.ttf". And we also replace the old font name variable with our new font name. 
The final result (for this part of the code) will look like this.
```python
    elif (font_clicked.get() == 'Gigi'):
        font_path = "C:\Windows\Fonts\GIGI.ttf"
        font_name = 'Gigi Regular'
        return font_name
        return font_path
```
From there we need to update the menu selection for our fonts
```python
optionsFont = [
    "Calibri",
    "Calibri",
    "Comic Sans",
    "Broadway",
    "STENCIL",
    "Blackadder ITC",
    "Magneto"
]
```
If you're adding a font, just of course add another selection. If replacing, replace the previous font with the new one.
The final thing we need to do to update this new font, is updating the menu to have it display the font when the user is selecting it. That'll be done in this section:
```python
# setting each font option to have it's corresponding style
dropDown["menu"].entryconfig(0, font=('Calibri', 12))
dropDown["menu"].entryconfig(1, font=('Comic Sans MS', 12))
dropDown["menu"].entryconfig(2, font=('Broadway', 12))
dropDown["menu"].entryconfig(3, font=('Stencil', 12))
dropDown["menu"].entryconfig(4, font=('Blackadder ITC', 12))
dropDown["menu"].entryconfig(5, font=('Magneto', 12))
```
Of course just replace 'Comic Sans MS', with 'Gigi Regular'. And that's all! TADA! You should now be able to use the new font with the application :).
