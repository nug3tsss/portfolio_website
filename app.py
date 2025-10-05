from flask import Flask, render_template, request

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
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

# "Area of a circle" PAGE
@app.route('/area-of-circle', methods=['GET', 'POST'])
def area_of_circle():
    return render_template('areaofcircle.html')

# "Area of a triangle" PAGE
@app.route('/area-of-triangle', methods=['GET', 'POST'])
def area_of_triangle():
    return render_template('areaoftriangle.html')

if __name__ == "__main__":
    app.run(debug=True)