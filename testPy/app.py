# print("test")
from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

global process

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    #script_path = './inference_classifier.py'
    
    # Execute the Python script using subprocess
    #subprocess.run(['python', script_path], capture_output=False, text=False, check=False)
    return render_template('learn.html')

@app.route('/startFun', methods=['POST'])
def startFun():
    process = subprocess.Popen(['python', './inference_classifier.py'])
    return redirect(url_for('/learn'))

@app.route('/stopFun', methods=['POST'])
def stopFun():
    process.terminate()
    #return redirect(url_for('index'))


@app.route('/run-script')
def run_script():
    # Replace 'your_script.py' with the path to your Python script
    script_path = './inference_classifier.py'
    
    # Execute the Python script using subprocess
    subprocess.run(['python', script_path], capture_output=False, text=False, check=False)

if __name__ == '__main__':
    app.run(debug=True)