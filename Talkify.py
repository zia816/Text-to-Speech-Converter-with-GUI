from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system("output.mp3")  # Corrected 'strat' to 'afplay'

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Start", command=textToSpeech)  # Removed parentheses after function name
canvas.create_window(200, 230, window=button)

root.mainloop()
