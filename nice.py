import clipboard
text = clipboard.paste()
lenght = len(text)
output = []
for i in range(lenght):
    if (i % 2) == 0:
        output.append(text[i].upper())
    else:
        output.append(text[i])
        
clipboard.copy(''.join(output))


