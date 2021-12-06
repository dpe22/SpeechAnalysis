Files to present for Sprint 4 EC601 Dec 1, 2021
## Sprint 4 Summary: Transfer learning using VGG16 and ResNet50
Transfer learning is a research problem in machine learning that focuses on storing knowledge gained while solving one problem and applying it to a different but related problem. Our VGG16 model is based on transfer learning from the ImageNet 1000-class photograph classification competition. Our goal is to create a COVID classification tool with more than 95% specificity and 90% sensitivity using machine learning.

## Sprint 4 Results:
ML Model   | Specificity  (MVP goal > 95.0%)   |  Sensitivity (MVP goal > 90%) | File Size
:---------------:|:-------------------------:|:-------------------------:|:---------------------:
VGG16 | 95 - 97% | 2 - 4% | 1.5 GB
ResNet50 | 58 - 62% | 45 - 49% | 270 MB

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
ResNet50 | ![resnet50confusion](https://user-images.githubusercontent.com/74585697/144291921-73aafa17-d5a6-475f-99f2-0e298702b164.png) | ![resnet50accuracy](https://user-images.githubusercontent.com/74585697/144291744-be0cf01f-77e4-447d-905a-6a6f7329619c.png) | ![resnet50loss](https://user-images.githubusercontent.com/74585697/144291835-8be987a2-5b2a-4517-88e2-391f04171dda.png)
EfficientNetB4 | | ![image](https://user-images.githubusercontent.com/74585697/144899524-434d680b-0469-4800-8013-ea1efb369531.png) | ![image](https://user-images.githubusercontent.com/74585697/144899455-76e8a402-9475-46a4-95a1-9c70b66fb06e.png) 



## What we would do with one more sprint
LSTM (Long Short Term Memory) RNN model

Improve signal preprocessing, feature extraction, and data cleaning

Combine datasets and machine learning models

