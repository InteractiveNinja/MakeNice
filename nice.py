import clipboard
import keyboard
import time
def makeNice():
    text = clipboard.paste()
    lenght = len(text)
    output = []
    for i in range(lenght):
        if (i % 2) == 0:
            output.append(text[i].upper())
        else:
            output.append(text[i])
            
    keyboard.write("".join(output))

keyboard.add_hotkey('ctrl+shift+ü',makeNice)


while keyboard.is_pressed('ctrl+shift+q') == False:
    time.sleep(0.2)
    
    
    