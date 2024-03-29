# ABOUT PROJECT

This project is a real-time pose detection and recognition system using the MediaPipe library and a pre-trained Keras neural network. 
The system is divided into three main files,

**1_data_collection.py:** This file is used to collect training data for the pose recognition model. It captures video frames from a webcam, detects the pose using the MediaPipe library, and saves the pose landmarks to a numpy file for later use.

![image](https://github.com/tiny-tachyon/INFIDATA/assets/144261872/7de163d8-f71d-4055-822d-d1a710b915fd)


**2_model_training.py:** This file trains a neural network model using the collected pose landmarks. It uses the Keras library to build and train a simple feedforward neural network with two hidden layers. The model is trained to recognize different yoga poses based on the pose landmarks.

![image](https://github.com/tiny-tachyon/INFIDATA/assets/144261872/00d7cde5-3551-4d0f-b3c6-6d5f61b51a00)


**3_inference.py:** This file is the main application that uses the trained model for real-time inference. It captures video frames from a webcam, detects the pose using the MediaPipe library, and feeds the pose landmarks into the trained model to recognize the pose. The recognized pose is displayed on the video frame in real-time.

[Demo screenshots come here...]

# HOW TO RUN

1. Clone the Repository(git clone)

2. Navigate to the Project Folder,
* Open a terminal or command prompt.
* Navigate to the folder where you extracted the repository using the cd command.
* Install Required Packages (pip install -r requirements.txt)

3. Execute **1_data_collection.py** (python 1_data_collection.py)

4. Execute **2_model_training.py** (python 1_data_collection.py)

5. Execute **3_inference.py** (python 1_data_collection.py)


The project can be used to learn and recognize different yoga poses in real-time, which can be helpful for yoga practitioners to improve their form and technique.
