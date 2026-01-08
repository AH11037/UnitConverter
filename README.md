# Unit Converter
This is a Flask-based web application that allows users to convert values between different units of **length, weight and temperature** through a simple and dynamic web interface. </br>
The project utilizes my **first tech stack** to provide a clean end-to-end conversion flow.
## Screenshots
### Home Page
<img width="198" height="270" alt="{3D3BCDAA-842C-4083-8006-89D071AC1DE7}" src="https://github.com/user-attachments/assets/a0d3733f-d240-4ed3-abaa-191b3d79144d" /> </br>
### Results Page
<img width="186" height="186" alt="{6473A34C-61A4-472D-859D-80B088F50DA8}" src="https://github.com/user-attachments/assets/04d6a59a-2ff2-469b-b5db-c574c9658f65" /> </br>
## Tech Stack
* Python
* Flask
* HTML
* Jinja2
## Supported Conversions
### Length
* Millimetre, centimetre, metre, kilometre
* Inch, foot, yard, mile
### Weight
* Milligrams, grams, kilograms
* Ounce, pound
### Temperature
* Celsius ↔ Fahrenheit
* Celsius ↔ Kelvin
* Fahrenheit ↔ Kelvin
## Web Interface
* Conversion type selection using navigation links
* Dynamic unit dropdowns that change based on selected category
* Clean result display with proper unit symbols
* Reset button to start a new conversion
* Visual indication of the selected conversion type
## Installation & Running
### Prerequisites
I don't want to call you stupid, but you **NEED** to have Python and Flask installed. </br>
1. Python is installed from the official Python website:</br>
   https://www.python.org
2. Flask is installed by running the command:
```
pip install flask
```
## Downloading & Running
1. Download the `.zip` file from `Releases`
2. Extract the contents of the file into a single folder
   * **DO NOT CHANGE HOW THE FOLDER IS STRUCTURED**
3. Open a terminal in that folder
4. Run the python file:
```
python unit-converter.py
```
5. Open a browser and go to:
```
http://127.0.0.1:5000
```
## How It Works
### Backend (`unit-converter.py`)
* Built using Flask
* Handles routing, form submissions and redirects
* Contains conversion logic for:
   * Length
   * Weight
   * Temperature
* Uses a centralised `convert_stuff()` function to process conversions
* Passes data to templates using Flask's render system
### Frontend (`index.html`)
* Acts as the main input page
* Allows users to:
   * Select conversion type (**Length**/**Weight**/**Temperature**)
   * Enter a numeric value
   * Choose source and target units
* Uses **Jinja conditionals** to dynamically update unit dropdowns based on the selected category
* Submits data via a POST request to the backend
### Result Page (`result.html`)
* Displays the converted value in a readable format
* Uses unit symbols (e.g. `km`, `kg`, `°C`) for clarity
* Preserves the selected conversion category for consistent navigation
* Provides a reset button to perform another conversion
## What I Learned
* Building web applications with Flask
* Handling form data using `request.form`
* Using query parameters to manage UI state
* Dynamic HTML rendering with Jinja templates
* Structuring conversion logic for multiple unit types
* Connecting backend logic with frontend UI flow
## Future Improvements
* Refactor conversion logic into cleaner, modular functions
* Remove global variables (I just learned these, give me a break)
* Add input validation and error handling
* Improve user experience with CSS
* Deploy the app online
