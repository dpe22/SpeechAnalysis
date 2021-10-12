# Product Mission
To provide an instantaneous, accessible, low-cost COVID-19 testing alternative that has high reliability and accuracy to help limit the spread of COVID-19. 

# Minimum Viable Product
An algorithmic model (ML?) to process the user's audio sample and diagnose COVID-19 with minimum of >90% sensitivity and >95% specificity and a target of >92% sensitivity and >99% specificity.

# MVP User Stories
As a person who wants to get tested for COVID-19 at any time in any location with access to a smartphone, I want to get my results instantly, with minimal cost, minimal travel distance, minimal interaction with other people (potential to infect others), as many times as I want,  with a high level of sensitivity (high true positive rate) and high specificity (high true negative rate) because I want to help limit the spread of COVID-19 from symptomatic individuals and prevent unnecessary death and hospitalization.

As a student or employee who is required to be tested for COVID-19 every week, I want to be able to complete my test without traveling to or having to schedule an appointment with the testing location. I want to complete my test without interacting with my roommates/family and others on campus/office in case I'm infected. I want to complete my test without the discomfort of sticking a swab up my nose, especially in dry weather. I need the test to be very fast because sometimes I procrastinate and I need the test to be very convenient to fit into my busy schedule. 

As a patient in a hospital or care facility, I know I already have been diagnosed with COVID, but I want to leave and get back to normal life as quickly as possible. I want a COVID-19 test that is repeatable without cost, and I need to be able to take the test without violating quarantine. I would appreciate a non-invasive method for daily testing. 

As an insurance company, medical provider, or government, I need to limit the spread of COVID-19 to keep medical facilities from being overwhelmed, prevent death and economic hardship, and I need to pay for any testing expense and damage that may result from the virus. I need an accurate COVID-19 test that is cheaper, easier to manufacture and distribute, and effective at stopping the spread of the virus. 

As a citizen of a developing nation, I cannot travel to a testing facility and I have not been offered a vaccine. I need a COVID-19 test that is free and accessible to me and others in my community so that we can work together to limit the spread of COVID without the infrastructure or government assistance provided in wealthier countries. 

Although the lack of electricity in some countries prevents the poorest citizens from owning or charging a mobile phone. Cell phones, and specifically smartphones are becoming more and more ubiquitous throughout the world. 

![image](https://user-images.githubusercontent.com/74585697/136975046-b508854f-037f-46df-877b-a6a71ee1d954.png)
Image Source (https://www.bankmycell.com/blog/how-many-phones-are-in-the-world)

It is our hope that this product might also help those in middle- and low-income countries who have limited access to vaccines and testing infrastructure but may have cell phone access.

![image](https://user-images.githubusercontent.com/74585697/136975821-d2eba02a-54f7-4503-bdbd-4b117d603682.png)
Image Source (https://www.linkedin.com/in/williamhgates/)

# Open-Source Data
The COUGHVID dataset provides over 25,000 crowdsourced cough recordings representing a wide range of participant ages, genders, geographic locations, and COVID-19 statuses. Four experienced physicians labeled more than 2,800 of the recordings.
  Measurement(s)	Cough
  Technology Type(s)	Microphone Device
  Factor Type(s)	COVID-19 status • location • age • gender • respiratory condition
  Sample Characteristic - Organism	Homo sapiens
Machine-accessible metadata file describing the reported data: https://doi.org/10.6084/m9.figshare.14377019
Open Source Research Paper https://www.nature.com/articles/s41597-021-00937-4

The XGB classifier used to remove non-cough recordings, feature extraction source code, cough preprocessing methods, cough segmentation function, and SNR estimation algorithm are available on a public repository: https://c4science.ch/diffusion/10770/repository

# What is Xgb regression?
Extreme Gradient Boosting is an open-source library that provides an efficient and effective implementation of the gradient boosting algorithm. It is called gradient boosting because it uses a gradient descent algorithm to minimize loss when adding new models. This approach supports both regression and classification predictive modeling problems.

# Machine Learning Technology
We are learning more about pytorch to better understand what libraries, tools and/or algorithms may be available to us to help us improve the classification of cough audio samples to diagnose COVID-19 and build our MVP.
