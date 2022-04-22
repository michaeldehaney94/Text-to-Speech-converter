from gtts import gTTS
import os
from tkinter import *


def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('text_audio.mp3')
    os.system('start text_audio.mp3')


root = Tk()
root.title('Text-to-Speech Convertor')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root, width=50)
canvas.create_window(200, 180, window=entry)

button = Button(text='Convert', fg='White', bg='Blue', command=lambda: textToSpeech())
canvas.create_window(200, 230, window=button)

root.mainloop()
