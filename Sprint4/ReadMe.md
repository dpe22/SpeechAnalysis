Files to present for Sprint 4 EC601 Dec 1, 2021
## Sprint 4 Summary: Transfer learning using VGG16 and ResNet50
Transfer learning is a research problem in machine learning that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem. Our VGG16 model is based on transfer learning from the ImageNet 1000-class photograph classification competition. Our goal is to create a COVID classification tool with more than 95% specificity and 90% sensitivity using machine learning.

## Sprint 4 Results:
ML Model   | Specificity  (MVP goal > 95.0%)   |  Sensitivity (MVP goal > 90%) | File Size
:---------------:|:-------------------------:|:-------------------------:|:---------------------:
VGG16 | 95 - 97% | 3.6% | 1.5 GB
ResNet50 | 60% | 47% | 270 MB

Specificity: The ratio of samples without covid that the model correctly predicts as negative

Sensitivity: The ratio of samples with covid that the model correctly predicts as positive


## Converting raw audio samples into spectrograms
Type    | Plain Spectrogram     |  MFCC |
:---------------:|:-------------------------:|:-------------------------:
COVID | ![image](https://user-images.githubusercontent.com/74585697/144285793-0fd55688-95ed-4703-aa18-e5364c369021.png)|![image](https://user-images.githubusercontent.com/74585697/144285865-28af373e-44d0-4126-b5a1-c3542ab32868.png)
HEALTHY | ![image](https://user-images.githubusercontent.com/74585697/144285938-829c52a3-ee88-48d9-aab1-ae1b255fff56.png)|![image](https://user-images.githubusercontent.com/74585697/144285986-352f57e0-a642-40cd-a2e1-420e88a296f6.png)


## ML Training Results
ML Model   | Confusion Matrix     |  Accuracy | Loss
:---------------:|:-------------------------:|:-------------------------:|:---------------------:
VGG16 | ![confusionVGG16](https://user-images.githubusercontent.com/74585697/144160213-22a3a5bc-d596-40c8-a6de-be4ab80080c9.png) | ![covidVGG16accuracy](https://user-images.githubusercontent.com/74585697/144160320-bf882314-a65f-40bb-8136-1b53ab534bf6.png) | ![covidVGG16loss](https://user-images.githubusercontent.com/74585697/144160601-25f3c118-2d12-4a1a-ba1f-0af5e1d3b97b.png)
ResNet50 | ![confusionResNet50](https://user-images.githubusercontent.com/74585697/144161272-8024bc2a-4901-400d-b588-6e41745184d9.png) | ![covidResNet50accuracy](https://user-images.githubusercontent.com/74585697/144161313-ca10ad59-e594-4912-9eeb-78194c2ac806.png) | ![covidResNet50loss](https://user-images.githubusercontent.com/74585697/144161329-5958d57b-3af9-434e-87eb-e267fe2c5a30.png) | NULL


## What we would do with one more sprint
LSTM (Long Short Term Memory) RNN model
Improve signal preprocessing, feature extraction, and data cleaning
Combine datasets and machine learning models

