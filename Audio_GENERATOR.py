from google_speech import Speech
from gtts import gTTS
import os

import random, string
list=[]
for i in range(1):
    r= ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    r = r.upper()
    if r not in list: list.append(r)

print(list)
lang = "en"
count = 0
for i in list:
    tts = gTTS('%s' %i)
    tts.save("./MP3/%s.wav" % i)

print("Done!")

