from flask import Flask, render_template, request, redirect, url_for, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Example route with parameters
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# Example API route
@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "Data received", "data": data}), 201
    return jsonify({"message": "Send some data using POST"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)