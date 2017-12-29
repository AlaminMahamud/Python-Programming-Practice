import pyperclip
text = pyperclip.paste()
text = text.split('\n')
list = ''
for s in text:
    list += ('* ' + s + '\n')
pyperclip.copy(list)
