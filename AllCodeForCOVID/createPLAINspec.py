import librosa as lb
from librosa.display import specshow
import python_speech_features
import matplotlib.pyplot as plt
from scipy.signal.windows import hann
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import splitfolders
import pandas as pd


def is_wav(filename):
    '''
        Checks if files are .wav files
        Utility tool in converting wav to png files
    '''
    return filename.split('.')[-1] == 'wav'

#create images using librosa spectogram
def convert_to_spec_image(file_loc, filename, category, is_train=False, verbose=False):
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
        print('reading and converting ' + filename + '...')
        
    y, sr = lb.load(loc)

    #Plot signal in
    plt.figure(figsize=(1.2,3))
    src_ft = lb.stft(y)
    src_db = lb.amplitude_to_db(abs(src_ft))
    specshow(src_db, sr=sr, x_axis=None, y_axis=None)  
    #plt.ylim(0, 10000)
    #plt.xlim(0,5)
    #plt.show()
    #breakpoint()
    save_directory = './specPLAIN/'
    filename_img = filename.split('.wav')[0]
    
    save_loc = save_directory + train_  + category + '/' + filename_img + '.png'
    if is_train == False:
        save_loc = save_directory + val_  + category +  '/' + filename_img + '.png'
        
    plt.savefig(save_loc)
    
    if verbose == True:
        print(filename + ' converted!')
        
    plt.close()




if __name__ == '__main__':
    #audio_loc = './WAV/'
    #splitfolders.ratio(audio_loc, output='./outputSpec', seed=1337, ratio=(0.8, 0.2))
    #breakpoint()
    files_loc = './WAVtrimsplit/'
    #diagnosis_csv = './metadata_compiled.csv'
    #diagnosis = pd.read_csv(diagnosis_csv, names=['uuid', 'status'])
    categories = ['COVID','Healthy']
    
    if os.path.exists('./specPLAIN'):
        pass
    else:
        os.makedirs('specPLAIN')
        os.makedirs('specPLAIN/train')
        os.makedirs('specPLAIN/val')
        for cat in categories:
            os.makedirs('specPLAIN/train/' + str(cat))
            os.makedirs('specPLAIN/val/' + str(cat))


    split = ['train', 'val']
    for s in split:
        for cat in categories:
            #print('-' * 100)
            #print('working on ' + cat + '...')
            #print('-' * 100)

            files = [f for f in listdir(files_loc + s + '/' + cat + '/') if isfile(join(files_loc + s + '/' + cat + '/', f)) and is_wav(f)]
            for f in files:
                print('running convert_to_spec')
                convert_to_spec_image(file_loc = files_loc, category = cat, filename=f, is_train=(s == 'train'), verbose=True)
