# Photo Album Technical Showcase

## Introduction

Photo album technical showcase is a program that retreives JSON data
from a web service, and displays data from each JSON object. 
I wrote this program as part of the application process for a 
position with Lean TECHniques, Inc. The requirements for the program
can be found in It-technical-showcases.pdf. 

## Technologies

The program is written in Python, Version 3.7. It uses the following libraries:
* requests
* json 
* re

The program retreives JSON data from the following 
web service: https://jsonplaceholder.typicode.com/photos

## Installing Python and running the program

Python can be installed on Windows or Linux using the following method.

### Install Anaconda Navigator

First, install Anaconda Navigator, a GUI package manager that includes 
a python instillation. It can be found here: 
https://docs.anaconda.com/anaconda/install/
After installing Anaconda Navigator, use it to 
install an IDE for writing python code. 

### Install Visual Studio Code

Use the Anaconda Navigator GUI to install Visual Studio Code. 
Set VS Code to use the python interpreter. Do this by selecting 
View->Command Palette, then the correct python version number. 
Then create a python workspace. 

### Creating a Python Workspace

Start by saving the current workspace. Then, go to File->Preferences->Settings.
Go to the user settings by selecting User, then Settings.JSON.
Copy the following line: "python.pythonPath": "<Your python path>".
Put the line into the workspace settings. To do this, open another settings tab 
by going to File->Preferences->Settings, and select workspace. 
Then select Settings.JSON. Paste the python path in the
following line: "settings": {<Paste python path line here>}.
The python environment is now set up. 

### Running the program

To run photo_album_technical_showcase.py, add the file to your workspace. 
Right click and select "Run Python File in Terminal".

## Sources

The instructions to install python came from the book
"Python All-in-One For Dummies (For Dummies (Computer/Tech))" 
by John Shovic and Alan Simpson. 

## Author

Thomas Staudt 