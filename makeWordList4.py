#This finally seems to work! Cobbled together from online sources, but...

import re
import pyperclip

file = open(r"C:\Users\user\Dropbox\KC BUSINESS\EE\Readings\writings21.txt", 'r')
# .lower() returns a version with all upper case characters replaced with lower case characters.
text = file.read().lower()
file.close()
# replaces anything that is not a lowercase letter, a space, or an apostrophe with a space:
text = re.sub('[^a-z\ \']+', " ", text)
for i in text.strip().split('\n'):
    for j in i.split():
        if len(j)>1:
            pyperclip.copy(j)
            print(j)
        
