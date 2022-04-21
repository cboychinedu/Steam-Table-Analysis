#!/usr/bin/env python3 

# Importing the necessary modules 
from flask import Blueprint, request 
from flask import render_template 
from TempModel.temp_analysis import TemperatureClassification 


# creating the blueprint for the temperature model 
temperature = Blueprint('temperature', __name__, 
                        template_folder="templates", 
                        static_folder="static")

# Creating the home page for the temperature route 
@temperature.route("/", methods=["GET", "POST"])
def Home(): 
    # Execute this block of code if the user navigates to 
    # the home page as a GET route 
    return render_template("temperature_home.html")

#  Making the predictions 
@temperature.route("/prediction", methods=["POST"])
def prediction(): 
    # Execute the block of code if the request is a "POST" request 
    # And create an instance of the temperature class 
    pred_temp = TemperatureClassification() 
    data = request.get_json() 

    # Making predictions 
    try: 
        # Grab the data from the post request, and perfom a ML analysis 
        # on the input data 
        data = float(data["pressure_value"])
        result = pred_temp.temperature(data)
        return { "result": result, "message": "success" }
    
    # On error, execute the block of code below 
    except:
        # Return the error as a result 
        return { "result": "Error in prediction", "message": "error" }; 