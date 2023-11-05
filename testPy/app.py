# print("test")
from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    #script_path = './inference_classifier.py'
    
    # Execute the Python script using subprocess
    #subprocess.run(['python', script_path], capture_output=False, text=False, check=False)
    return render_template('learn.html')

@app.route('/start_script', methods=['POST'])
def start_script():
        global process
    #if process is None or process.returncode is not None:
        process = subprocess.Popen(['python', './inference_classifier.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify(success=True)
        return jsonify(success=False)

@app.route('/stop_script', methods=['POST'])
def stop_script():
    #global process
        global process
    #if process and process.returncode is None:
        process.terminate()
        return jsonify(success=True)
    #return jsonify(success=False)

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