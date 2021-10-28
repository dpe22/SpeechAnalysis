
import scipy
import librosa



import matplotlib
import matplotlib.pyplot as plt

import time


from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav



def plot_spectrogram(spec, title=None, ylabel='freq_bin', aspect='auto', xmax=None):
  fig, axs = plt.subplots(1, 1)
  axs.set_title(title or 'Spectrogram (db)')
  axs.set_ylabel(ylabel)
  axs.set_xlabel('frame')
  im = axs.imshow(librosa.power_to_db(spec), origin='lower', aspect=aspect)
  if xmax:
    axs.set_xlim((0, xmax))
  fig.colorbar(im, ax=axs)
  plt.show(block=True)

if __name__ == "__main__":
  SAMPLE_WAV_PATH = "/media/james/extradrive1/homework/homework/EC601/SpeechAnalysis/Preprocessing/cough.wav"
  (rate,sig) = wav.read(SAMPLE_WAV_PATH)

  mfcc_feat = mfcc(sig,rate,winlen = 0.008,winstep=0.003) 
  plot_spectrogram(mfcc_feat) 

