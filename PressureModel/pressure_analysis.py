#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
import joblib 
import numpy as np 
import tensorflow.compat.v1 as tf 
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


# Disable tensorflow version 2 behavior 
tf.disable_v2_behavior() 

# Creating a class for deep neural networks linear regression model using 
# tensorflow models 
class PressureClassification:
    def __init__(self):
        # Getting the path to the current working directory, the model dir, 
        # the pressure model, and the input temperature value.
        self.root_path = os.getcwd() 
        self.model_dir = os.path.sep.join([self.root_path, "models"])
        self.pressure_model = os.path.sep.join([self.model_dir, "pressureModel.h5"])

        # Setting the path to the pressure, and temperature encoders.
        self.pressure_encoder = os.path.sep.join([self.model_dir, "pressure_encoder.bin"])
        self.temp_encoder = os.path.sep.join([self.model_dir, "temperature_encoder.bin"]) 
        

    # Creating a method for building the neural network model 
    def build_model(self):
        # Building the neural network model 
        model = Sequential() 
        model.add(Dense(250, input_dim=1))
        model.add(Dense(150, activation="relu")) 
        model.add(Dense(120, activation="relu"))
        model.add(Dense(32, activation="relu"))
        model.add(Dense(8, activation="relu"))
        model.add(Dense(1))

        # Return the model weighted file 
        return model 

    # Creating a method for performing mathematical calculations on the 
    # temperature value, and returning the predicted calculations 
    def pressure(self, temperature_value=0.00):
        # This method function is to make pressure predictions from the 
        # input temperature values. 
        # It loads the serialized neural network model into memory, encodes 
        # the input temperature values, and then gives the predicted value 
        # in pressure readings 
        # Creating an instance of the model 
        model = self.build_model() 
        model.compile(loss="mean_squared_error", optimizer="sgd"); 

        # Load the save weights from disk in the models directory 
        model.load_weights(self.pressure_model)

        # Loading the encoders 
        pressure_enc = joblib.load(self.pressure_encoder)
        temperature_enc = joblib.load(self.temp_encoder)

        # Transform the input value, which in this situatuon is the 
        # temperature value into a numpy array, then encode the values 
        temperature_value = float(temperature_value)
        temperature = np.array([temperature_value]).reshape(1, -1)
        temperature = temperature_enc.transform(temperature)

        # Making predictions on the transformed temperature value 
        prediction = model.predict(temperature)
        prediction = pressure_enc.inverse_transform(prediction)
        prediction = prediction[0][0]
        prediction = "{:.2f}".format(prediction)

        # Return the predicted pressure value as a JSON object 
        prediction = {"predictedPressure": prediction }
        return prediction; 