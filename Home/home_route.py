#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
from flask import Blueprint, request 
from flask import render_template 

# Creating the blueprint for the home page 
home = Blueprint('home', __name__, template_folder='templates', static_folder='static')

# Creating the home page 
@home.route('/', methods=["GET"])
def Home(): 
    # 
    return render_template("home.html")