from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return render_template_string('''
        <h1>Python Operations with Flask Routing and Views</h1>
    ''')

# Print string route
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  # Print to console
    return f'<h2>Printed: {parameter}</h2>'

# Count route
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '<br>'.join(str(i) for i in range(parameter + 1))  # Create a string of numbers
    return f'<h2>Counting to {parameter}:</h2><pre>{numbers}</pre>'

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else 'Division by zero error'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation!', 400
    
    return f'<h2>Result of {num1} {operation} {num2} = {result}</h2>'

if __name__ == '__main__':
    app.run(debug=True)