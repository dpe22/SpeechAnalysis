from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D , Flatten,GlobalAveragePooling2D
from tensorflow.keras.losses import categorical_crossentropy
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping,TensorBoard,ReduceLROnPlateau
from tensorflow.keras import metrics

from sklearn.utils import class_weight
from collections import Counter

import matplotlib.pyplot as plt

from os import listdir
from os.path import isfile, join

import pandas as pd


train_loc = './specimages/train_test_split/train/'
test_loc = './specimages/train_test_split/val/'

trdata = ImageDataGenerator()
traindata = trdata.flow_from_directory(directory=train_loc, target_size=(224,224))
tsdata = ImageDataGenerator()
testdata = tsdata.flow_from_directory(directory=test_loc, target_size=(224,224))
diagnosis_csv = './respiratory-sound-database/respiratory_sound_database/Respiratory_Sound_Database/patient_diagnosis.csv'
diagnosis = pd.read_csv(diagnosis_csv, names=['pId', 'diagnosis'])
categories = diagnosis['diagnosis'].unique()


base_model = ResNet50(weights='imagenet',include_top=False,input_shape= (224,224,3))
#base_model.summary()

x  = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.7)(x)
predictions = Dense(8, activation= 'softmax')(x)
model = Model(inputs = base_model.input, outputs = predictions)
adam = Adam(lr=0.0000001)
model.compile(optimizer= adam, loss='categorical_crossentropy', metrics=['accuracy'])
#model.summary()
checkpoint = ModelCheckpoint("rn_base_res.h5", monitor='val_accuracy', verbose=2, 
                             save_best_only=True, save_weights_only=False, mode='auto')
early = EarlyStopping(monitor='val_accuracy', min_delta=0, patience=20, verbose=2, mode='auto')
counter = Counter(traindata.classes)                       
max_val = float(max(counter.values()))   
class_weights = {class_id : max_val/num_images for class_id, num_images in counter.items()}
hist = model.fit(traindata, steps_per_epoch=traindata.samples//traindata.batch_size, validation_data=testdata, 
                 class_weight=class_weights, validation_steps=testdata.samples//testdata.batch_size, 
                 epochs=100,callbacks=[checkpoint,early])
#hist = model.fit(traindata, epochs = 100, batch_size = traindata.batch_size)

breakpoint()
 

plt.plot(hist.history['loss'], label='train')
plt.plot(hist.history['val_loss'], label='val')
plt.title('ResNet50: Loss and Validation Loss (0.000001 = Adam LR)')
plt.legend();
plt.show()

plt.plot(hist.history['accuracy'], label='train')
plt.plot(hist.history['val_accuracy'], label='val')
plt.title('ResNet50: Accuracy and Validation Accuracy (0.000001 = Adam LR)')
plt.legend();
plt.show()


