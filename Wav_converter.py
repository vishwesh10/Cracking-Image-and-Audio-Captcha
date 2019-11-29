import os
from pydub import AudioSegment

path = "./KritiAudio/"

#Change working directory
os.chdir(path)
audio_files = os.listdir()

# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    #if ext == ".mp3" and os.path.exists('../MP3/{0}.wav'.format(name)) == False:
    mp3_sound = AudioSegment.from_mp3(file)
       #rename them using the old name + ".wav"
    mp3_sound.export("../GEN/{0}.wav".format(name), format="wav")
    print("Image with label {0} Processed.".format(name))
print("DONE!")
