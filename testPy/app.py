from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to your Flask application"

@app.route('/run-script')
def run_script():
    # Replace 'your_script.py' with the path to your Python script
    script_path = 'inference_classifier.py'
    
    # Execute the Python script using subprocess
    subprocess.run(['python', script_path], capture_output=False, text=False, check=False)

if __name__ == '__main__':
    app.run(debug=True)