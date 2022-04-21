#!/usr/bin/env python3 

# Importing the necessary modules 
from flask import Blueprint, request  
from flask import render_template 
from PressureModel.pressure_analysis import PressureClassification


# Creating the blueprint for the pressure model 
pressure = Blueprint('pressure', __name__, 
                    template_folder="templates",
                    static_folder="static")

# Creating the home page for the pressure route 
@pressure.route("/", methods=["GET"])
def Home():
    # Execute this block of code if the user navigates to 
    # the home page as a GET route 
    return render_template("pressure_home.html")

# Make predictions 
@pressure.route("/prediction", methods=["POST"])
def predictions():
    # Execute the block of code if the request is a "POST" request 
    # elif request.method == "POST":
    # Creating an instance of the pressure class 
    pred_pressure = PressureClassification() 
    data = request.get_json()

    # Making the predictions 
    try:
        # Grab the data from the post request, and perfom a ML analysis 
        # on the input data 
        data = float(data["temp_value"]) 
        result = pred_pressure.pressure(data) 
        return { "result": result, "message": "success"}

    # On error, execute the block of code below 
    except:
        # Return the error result 
        return { "result": "Error in prediction", "message": "error"}; 