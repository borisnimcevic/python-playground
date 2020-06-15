#! python3
# Adds wikipedia bulet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
	lines[i]= '*' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
