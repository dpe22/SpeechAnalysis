import librosa as lb
from librosa.display import specshow
import python_speech_features
import matplotlib.pyplot as plt
from scipy.signal.windows import hann
import os
from os import listdir
from os.path import isfile, join
import numpy as np

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
    
    loc = file_loc + train_ + category + '/' + filename
    if is_train == False:
        loc = file_loc + val_ + category + '/' + filename

    if verbose == True:
        print('reading and converting ' + filename + '...')
        
    y, sr = lb.load(loc)


        #Convert audio to mfcc
    n_mfcc = 13
    n_mels = 40
    n_fft = 512
    hop_length = 160 #smaples
    fmin = 0
    fmax = None
    mfcc_speech = python_speech_features.mfcc(signal=y, samplerate=sr, winlen=n_fft / sr, winstep=hop_length / sr,
                                          numcep=n_mfcc, nfilt=n_mels, nfft=n_fft, lowfreq=fmin, highfreq=fmax,
                                          preemph=0.0, ceplifter=0, appendEnergy=False, winfunc=hann)
    mfcc_speech= np.swapaxes(mfcc_speech, 0 ,1)
    specshow(mfcc_speech,sr=sr)
    plt.axis('off')
    plt.show()
    breakpoint()
    save_directory = 'output/'
    filename_img = filename.split('.wav')[0]
    
    save_loc = save_directory + train_ + category + '/' + filename_img + '.png'
    if is_train == False:
        save_loc = save_directory + val_ + category + '/' + filename_img + '.png'
        
    plt.savefig(save_loc, bbox_inches="tight")
    #breakpoint()
    if verbose == True:
        print(filename + ' converted!')
        
    plt.close()




if __name__ == '__main__':
    files_loc = './cnn-part-2-split-to-train-and-test/output/'
    diagnosis_csv = './respiratory-sound-database/respiratory_sound_database/Respiratory_Sound_Database/patient_diagnosis.csv'
    diagnosis = pd.read_csv(diagnosis_csv, names=['pId', 'diagnosis'])
    categories = diagnosis['diagnosis'].unique()
    if os.path.exists('./output'):
        pass
    else:
        os.makedirs('output')
        os.makedirs('output/train')
        os.makedirs('output/val')
        for cat in categories:
            os.makedirs('output/train/' + cat)
            os.makedirs('output/val/' + cat)

    split = ['train', 'val']
    for s in split:
        for cat in categories:
            #print('-' * 100)
            #print('working on ' + cat + '...')
            #print('-' * 100)

            files = [f for f in listdir(files_loc + s + '/' + cat + '/') if isfile(join(files_loc + s + '/' + cat + '/', f)) and is_wav(f)]
            for f in files:
                convert_to_spec_image(file_loc = files_loc, category=cat, filename=f, is_train=(s == 'train'), verbose=True)