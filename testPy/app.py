# print("test")
from flask import Flask, render_template, request, jsonify
from flask_sse import sse

import subprocess

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/aboutTest")
def aboutTest():
    return render_template("aboutTest.html")


@app.route("/learn")
def learn():
    # script_path = './inference_classifier.py'

    # Execute the Python script using subprocess
    # subprocess.run(['python', script_path], capture_output=False, text=False, check=False)
    return render_template("learn.html")


@app.route("/start_script", methods=["POST"])
def start_script():
        global process
    #if process is None or process.returncode is not None:
        process = subprocess.Popen(['python', './inference_classifier.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify(success=True)


@app.route("/stop_script", methods=["POST"])
def stop_script():
    #global process
        global process
    #if process and process.returncode is None:
        process.terminate()
        return jsonify(success=True)

@app.route('/start_test', methods=['POST'])
def start_test():
        global processTest
    #if process is None or process.returncode is not None:
        processTest = subprocess.Popen(['python', './practiceTest.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify(success=True)

@app.route('/stop_test', methods=['POST'])
def stop_test():
    #global process
        global processTest
    #if process and process.returncode is None:
        processTest.terminate()
        return jsonify(success=True)

@app.route("/run-script")
def run_script():
    # Replace 'your_script.py' with the path to your Python script
    script_path = "./inference_classifier.py"

    # Execute the Python script using subprocess
    subprocess.run(
        ["python", script_path], capture_output=False, text=False, check=False
    )


@app.route('/practice')
def practice():
    script_path = './inference_classifier.py'
    return render_template('practice.html')
    
@app.route('/stream')
def stream():
    return sse(sse_id='stream', retry=1000)

if __name__ == '__main__':
    app.run(debug=True)
