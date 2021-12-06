import librosa as lb
from librosa.display import specshow
#import python_speech_features
#import matplotlib.pyplot as plt
from scipy.signal.windows import hann
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import splitfolders
import pandas as pd
import soundfile as sf

def is_wav(filename):
    '''
        Checks if files are .wav files
        Utility tool in converting wav to png files
    '''
    return filename.split('.')[-1] == 'wav'

#trim audio silence at beginning and end using librosa
def split_WAV(file_loc, filename, category, is_train=False, verbose=False):
    ''' 
        Converts audio file to spec image
        Input file includes path
        Saves the file to a png image in the save_directory
    '''
    train_ = 'train/'
    val_ = 'val/'
    
    loc = file_loc + train_ + cat + '/' + filename
    print(loc)
    if is_train == False:
        loc = file_loc + val_ + cat + '/' + filename

    if verbose == True:
        print('reading and splitting ' + filename + '...')
        
    y, sr = lb.load(loc,sr = None)
    #print(y.shape)
    #breakpoint()
    #Plot signal in
    #plt.figure(figsize=(5,3))
    #src_ft = lb.stft(y)
    #src_db = lb.amplitude_to_db(abs(src_ft))
    #specshow(src_db, sr=sr, x_axis='time', y_axis='hz')  
    #plt.ylim(0, 5000)
    #plt.xlim(2,5)
    #plt.show()
    #breakpoint()

    # Trim the beginning and ending silence
    #yt, index = lb.effects.trim(y,top_db = 20)

    # Split the audio sample and delete segments where signal strength falls more than 30db below peak
    intervals = lb.effects.split(y, top_db=30)

    save_directory = './WAVtrimsplit/'
    filename_img = filename.split('.wav')[0]
    for i in range(len(intervals)):
        save_loc = save_directory + train_  + category + '/' + filename_img + '_' + str(i) + '.wav'
        if is_train == False:
            save_loc = save_directory + val_  + category +  '/' + filename_img + '_' + str(i) + '.wav'
        
        if ((intervals[i][1] - intervals[i][0]) > 6000):
            yt = y[intervals[i][0] : intervals[i][1]]
            #print(intervals[0][1] - intervals[0][0])
            sf.write(save_loc, yt, sr, 'PCM_24')
    #plt.savefig(save_loc)
    
    if verbose == True:
        print(filename + ' split!')
    #breakpoint()
    #plt.close()




if __name__ == '__main__':
    #audio_loc = './WAV/'
    #splitfolders.ratio(audio_loc, output='./outputSpec', seed=1337, ratio=(0.8, 0.2))
    #breakpoint()
    files_loc = './WAVtrimmed/'
    #diagnosis_csv = './metadata_compiled.csv'
    #diagnosis = pd.read_csv(diagnosis_csv, names=['uuid', 'status'])
    categories = ['COVID','Healthy']
    
    if os.path.exists('./WAVtrimsplit'):
        pass
    else:
        os.makedirs('WAVtrimsplit')
        os.makedirs('WAVtrimsplit/train')
        os.makedirs('WAVtrimsplit/val')
        for cat in categories:
            os.makedirs('WAVtrimsplit/train/' + cat)
            os.makedirs('WAVtrimsplit/val/' + cat)


    split = ['train', 'val']
    for s in split:
        for cat in categories:
            #print('-' * 100)
            #print('working on ' + cat + '...')
            #print('-' * 100)

            files = [f for f in listdir(files_loc + s + '/' + cat + '/') if isfile(join(files_loc + s + '/' + cat + '/', f)) and is_wav(f)]
            for f in files:
                print('running split_WAV')
                split_WAV(file_loc = files_loc, category = cat, filename=f, is_train=(s == 'train'), verbose=True)
