from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operation):
    """Performs basic arithmetic operations."""
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero"
    except ValueError:
        return "Error: Invalid input"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")
        
        result = calculate(num1, num2, operation)
        
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
