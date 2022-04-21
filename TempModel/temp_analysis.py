#!/usr/bin/env python3 

# Importing the necessay modules 
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
class TemperatureClassification: 
    def __init__(self):
        # Getting the path to the current working directory, the model directory, 
        # the temperature model, and the input pressure value 
        self.root_path = os.getcwd() 
        self.model_dir = os.path.sep.join([self.root_path, "models"]) 
        self.temp_model = os.path.sep.join([self.model_dir, "temperatureModel.h5"])

        # Setting the path to the pressure, and temperature encoders.
        self.pressure_encoder = os.path.sep.join([self.model_dir, "pressure_encoder.bin"])
        self.temp_encoder = os.path.sep.join([self.model_dir, "temperature_encoder.bin"])

    
    # Creating a method for building the neural network model in tensorflow
    # for temperature 
    def build_model(self):
        # Building the neural network model   
        model = Sequential() 
        model.add(Dense(250, input_dim=1))
        model.add(Dense(150, activation="relu")) 
        model.add(Dense(120, activation="relu"))
        model.add(Dense(32, activation="relu")) 
        model.add(Dense(1)) 
        
        # Returning the model
        return model

    # Creating a method for performing mathematical calculations on the 
    # pressure value, and returning the predicted calculations to the user
    def temperature(self, pressure_value=0.00):
        # This method function is to make temperature predictions from the 
        # input pressure values. 
        # it loads the serialized neural network model into memory, encodes the 
        # input pressure values, and then gives the predicted value in temperature readings. 
        # Creating an instance of the model 
        model = self.build_model()
        model.compile(loss="mean_squared_error", optimizer="sgd"); 

        # Load the save weights from disk into the models directory 
        model.load_weights(self.temp_model)

        # Loading the encoders 
        pressure_enc = joblib.load(self.pressure_encoder)
        temperature_enc = joblib.load(self.temp_encoder)

        # Transform the input value, which in this situation is the 
        # pressure value into a numpy array, and then encode the values 
        pressure_value = float(pressure_value)
        pressure = np.array([pressure_value]).reshape(1, -1)
        pressure = pressure_enc.transform(pressure)

        # Making predictions on the transformed pressure value 
        prediction = model.predict(pressure) 
        prediction = temperature_enc.inverse_transform(prediction)
        prediction = prediction[0][0]
        prediction = "{:.2f}".format(prediction) 

        # Return the predicted temperature value as a JSON object 
        prediction = { "predictedTemp": prediction }
        return prediction;  