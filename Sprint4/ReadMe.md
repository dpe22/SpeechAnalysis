Files to present for Sprint 4 EC601 Dec 1, 2021
## Healthy vs COVID cough images (plain vs MFCC)
Status    | Plain Spectrogram     |  MFCC |
:---------------:|:-------------------------:|:-------------------------:
COVID | ![image](https://user-images.githubusercontent.com/74585697/144285793-0fd55688-95ed-4703-aa18-e5364c369021.png)|![image](https://user-images.githubusercontent.com/74585697/144285865-28af373e-44d0-4126-b5a1-c3542ab32868.png)
HEALTHY | ![image](https://user-images.githubusercontent.com/74585697/144285938-829c52a3-ee88-48d9-aab1-ae1b255fff56.png)|![image](https://user-images.githubusercontent.com/74585697/144285986-352f57e0-a642-40cd-a2e1-420e88a296f6.png)

## VGG16 Results

###### Specificity 
96.8%  (MVP goal > 95.0%)
The ratio of samples without covid that the model correctly predicts as negative

###### Sensitivity 
3.6%  (MVP goal > 90%)
The ratio of samples with covid that the model correctly predicts as positive

###### Confusion Matrix
![confusionVGG16](https://user-images.githubusercontent.com/74585697/144160213-22a3a5bc-d596-40c8-a6de-be4ab80080c9.png)

###### Validation Accuracy
![covidVGG16accuracy](https://user-images.githubusercontent.com/74585697/144160320-bf882314-a65f-40bb-8136-1b53ab534bf6.png)

###### Loss
![covidVGG16loss](https://user-images.githubusercontent.com/74585697/144160601-25f3c118-2d12-4a1a-ba1f-0af5e1d3b97b.png)


## ResNet50 Results

###### Specificity 
60%  (MVP goal > 95.0%)
The ratio of samples without covid that the model correctly predicts as negative

###### Sensitivity 
47%  (MVP goal > 90%)
The ratio of samples with covid that the model correctly predicts as positive

###### Confusion Matrix
![confusionResNet50](https://user-images.githubusercontent.com/74585697/144161272-8024bc2a-4901-400d-b588-6e41745184d9.png)

###### Validation Accuracy
![covidResNet50accuracy](https://user-images.githubusercontent.com/74585697/144161313-ca10ad59-e594-4912-9eeb-78194c2ac806.png)

###### Loss
![covidResNet50loss](https://user-images.githubusercontent.com/74585697/144161329-5958d57b-3af9-434e-87eb-e267fe2c5a30.png)
