import os
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical

from keras.layers import Input, Dense
from keras.models import Model

is_initialized = False
size_data = -1

label_names = []
label_dict = {}
class_count = 0

# Iterate over files in the directory
for file_name in os.listdir():
    # Check if the file is a numpy file and not the label file
    if file_name.split(".")[-1] == "npy" and not (file_name.split(".")[0] == "labels"):
        # Load the data from the numpy file
        if not (is_initialized):
            is_initialized = True
            X_data = np.load(file_name)
            size_data = X_data.shape[0]
            y_data = np.array([file_name.split('.')[0]] * size_data).reshape(-1, 1)
        else:
            X_data = np.concatenate((X_data, np.load(file_name)))
            y_data = np.concatenate((y_data, np.array([file_name.split('.')[0]] * size_data).reshape(-1, 1)))

        # Store the class name in the list
        label_names.append(file_name.split('.')[0])
        # Store the class name and index in the dictionary
        label_dict[file_name.split('.')[0]] = class_count
        class_count += 1

# Convert the class labels to categorical format
for i in range(y_data.shape[0]):
    y_data[i, 0] = label_dict[y_data[i, 0]]
y_data = np.array(y_data, dtype="int32")

y_data = to_categorical(y_data)

X_new_data = X_data.copy()
y_new_data = y_data.copy()
counter_data = 0

# Shuffle the data
count_arr = np.arange(X_data.shape[0])
np.random.shuffle(count_arr)

# Rearrange the data based on the shuffled indices
for i in count_arr:
    X_new_data[counter_data] = X_data[i]
    y_new_data[counter_data] = y_data[i]
    counter_data += 1

#creating an ANN model
input_layer = Input(shape=(X_data.shape[1]))
model_layer = Dense(128, activation="tanh")(input_layer)
model_layer = Dense(64, activation="tanh")(model_layer)
output_layer = Dense(y_data.shape[1], activation="softmax")(model_layer)
model = Model(inputs=input_layer, outputs=output_layer)

#compiling the model
model.compile(optimizer='rmsprop', loss="categorical_crossentropy", metrics=['acc'])

#training the model
model.fit(X_new_data, y_new_data, epochs=80)

model.save("trained_model.h5")#saving the trained model
np.save("class_labels.npy", np.array(label_names))

print('MODEL TRAINING COMPLETE...')
