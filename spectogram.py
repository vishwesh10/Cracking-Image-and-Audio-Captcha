

import os
import librosa.display
import librosa.feature
import numpy as np
import matplotlib.pyplot as plt
count = 0
train_audio_path = './GEN/'
labels = os.listdir(train_audio_path)
print("Total Files: {0}".format(len(labels)))
for label in labels:
    def extract_mfcc(file, fmax, nMel):
        y, sr = librosa.load(in_path + label)
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=nMel, fmax=fmax)
        plt.figure(figsize=(3, 3), dpi=100)
        librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), fmax=fmax)
        plt.xticks([])
        plt.yticks([])
        plt.tight_layout()
        plt.savefig('./Kritiimage/' + file[:-3] + 'png', bbox_inches='tight', pad_inches=-0.1)

        plt.close()
        return
    in_path = './GEN/'
    S = extract_mfcc(label, 8000, 256)
    count += 1
    if count % 20 == 0:
        print ('%d files processed.' % count)

print ('Done!\t%d files processed.' % count)
