## Code Description 

###### pre processing 
convert.py : convert .ogg and .webm to .wav
trimWAV.py : trim beginning and ending silence (20db below peak)
splitWAV.py : split into individual cough sample and trim silence (30db below peak)
###### Feature Extraction
create-mfcc-images.py : create mfcc of cough samples
creatPLANspec.py : create short time Fourier Transform of cough smaples
###### Train Models
covid-efficientnet.ipynb : Use efficientnetB4 model to diagnose COVID
covid_res50.ipynb : Use ResNet50 model to diagnose COVID
covid_vgg16.ipynb : Use VGG16 model to diagnose COVID
