# Python daily tracker script

# Setup
PyInstaller is used to turn our .py file into an executable we can run by simply clicking on it.
pip install pyinstaller
py -m PyInstaller --onefile tracking.py

# About & Usage
The program is very simple, essentially consisting of a list of variables we wish to track and corresponding prompts (edit these to your liking in the .py file). 
Upon completion, the script saves the entered values into an Excel document.
A lot of the codebase exists to give flexibility, allowing the user to skip certain values and come back later in the day to fill them out, 
or to add values over the course of the day (useful in the case of calories for instance).

* Build the script using the setup commands outlined above.
* Run the script by simply double-clicking the .exe file
* Select whether you wish to alter the previous entry or make a new one.
* Enter values for variables you wish to track, pressing enter after each (pressing enter without providing a value saves a zero, e.g., zero drinks consumed).
* You can always come back and alter values provided, though the current version only supports addition (entering 50 adds 50 to the pre-existing value)

# Utility
I wrote the program to track daily habits I had trouble sticking to otherwise, such as forgetting to take my creatine. Making a limited though perfectly sufficient 
python script was my way of leveraging the sunk cost fallacy to compel myself to use it and commit to tracking. The Hawthrone effect (people behave differently when observed, or tracked
in this case) then takes care of the gaps in creatine supplementation or daily reading goals or whatever else you wish to track.
