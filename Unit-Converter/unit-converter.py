from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def convert_stuff(value, from_unit, to_unit,type = ['Length', 'Weight', 'Temperature']):
    if type == 'Length':
        conversions = {
        'meter': 1,
        'kilometer':0.001,
        'mile':0.000621371,
        'foot':3.28084,
        'inch':39.3701,
        'centimeter':100,
        'millimeter':1000,
        'yard':1.093613,
    }
    if type == 'Weight':
        conversions = {
        'grams':1,
        'kilograms':0.001,
        'ounce':0.03527396,
        'pound':0.002204623,
        'milligram':1000,
    }
    if type == 'Temperature':
        conversions = {
        'celsius':('celsius', 'fahrenheit', lambda c:(c * 9/5)+ 32, lambda f:(f-32)*5/9),
        'fahrenheit':('fahrenheit', 'celsius', lambda f: (f - 32) * 5/9, lambda c: (c * 9/5) + 32),
        'kelvin': ('kelvin', 'celsius', lambda k: k - 273.15, lambda c: c + 273.15),
        'fahrenheit_to_kelvin': ('fahrenheit', 'kelvin', lambda f: (f - 32) * 5/9 + 273.15, lambda k: (k - 273.15) * 9/5 + 32),
    }
    if from_unit in conversions and to_unit in conversions:
        if from_unit in ['celsius', 'fahrenheit', 'kelvin'] and to_unit in ['celsius', 'fahrenheit','kelvin']:
            if from_unit == 'celsius':
                if to_unit == 'fahrenheit':
                    return conversions[to_unit][3](value)
                elif to_unit == 'kelvin':
                    return conversions[to_unit][3](value)
                else:
                    return value
            elif from_unit == 'fahrenheit':
                if to_unit == 'celsius':
                    return conversions[from_unit][2](value)
                elif to_unit == 'kelvin':
                    return conversions['fahrenheit_to_kelvin'][2](value)
                else:
                    return value
            else:
                if to_unit == 'celsius':
                    return conversions[from_unit][2](value)
                elif to_unit == 'fahrenheit':
                    return conversions['fahrenheit_to_kelvin'][3](value)
                else:
                    return value
        else:
            return value * conversions[to_unit]/conversions[from_unit]
    else:
        return "Try again and input the correct units"

@app.route('/', methods = ['GET', 'POST'])
def index():
    global value
    global from_unit
    global to_unit
    global result
    global conversion_type
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']
        conversion_type = request.args.get('option')
        result = convert_stuff(value, from_unit, to_unit, conversion_type)
        return redirect(url_for('result'))
    return render_template('index.html')

@app.route('/result', methods = ['GET'])
def result():
    units = {
        'meter': 'm',
        'kilometer': 'km',
        'mile': 'mi',
        'foot': 'ft',
        'inch': 'in',
        'centimeter': 'cm',
        'millimeter': 'mm',
        'yard': 'yd',
        'grams': 'g',
        'kilograms': 'kg',
        'ounce': 'oz',
        'pound': 'lb',
        'milligram': 'mg',
        'celsius': '°C',
        'fahrenheit': '°F',
        'kelvin': 'K'
    }
    return render_template('result.html', output=result,value = value, from_unit = from_unit, to_unit= to_unit, units = units, option = conversion_type)

if __name__ == '__main__':
    app.run(debug=True)