from flask import Flask, render_template, request
import math

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('home.html')

# PROFILE PAGE
@app.route('/profile')
def profile():
    return render_template('profile.html')

# CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template('contact.html')

# WORKS PAGE
@app.route('/works')
def works():
    return render_template('works.html')

# "Convert to uppercase" PAGE
@app.route('/to-uppercase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('input_string', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

# "Area of a circle" PAGE
@app.route('/area-of-circle', methods=['GET', 'POST'])
def area_of_circle():
    result = None
    if request.method == 'POST':
        input_radius = float(request.form.get('input_radius', 0))
        result = round((math.pi * math.pow(input_radius, 2)), 2)
    return render_template('areaofcircle.html', result=result)

# "Area of a triangle" PAGE
@app.route('/area-of-triangle', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        input_base = float(request.form.get('input_base', 0))
        input_height = float(request.form.get('input_height', 0))
        result = round((0.5 * input_base * input_height), 2)
    return render_template('areaoftriangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)