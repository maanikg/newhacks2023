# print("test")
from flask import Flask, render_template, request, jsonify, Response
import time
import sys

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

    # Execute the python3 script using subprocess
    # subprocess.run(['python3', script_path], capture_output=False, text=False, check=False)
    return render_template("learn.html")


@app.route("/start_script", methods=["POST"])
def start_script():
    global process
    # if process is None or process.returncode is not None:
    process = subprocess.Popen(
        ["python3", "./inference_classifier.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return jsonify(success=True)


@app.route("/stop_script", methods=["POST"])
def stop_script():
    # global process
    global process
    # if process and process.returncode is None:
    process.terminate()
    return jsonify(success=True)


processTest = None


@app.route("/start_test", methods=["POST"])
def start_test():
    global processTest
    # if process is None or process.returncode is not None:
    # with open("output.txt", "a") as f:
    # processTest = subprocess.Popen(
    #     ["python3", "./practiceTest.py"],
    #     # stdout=subprocess.PIPE,
    #     # stdout=subprocess.STDOUT,
    #     stdout=None,
    #     # stderr=subprocess.PIPE,
    #     # stderr=None,
    #     stderr=None,
    #     # stderr=subprocess.STDOUT,
    #     text=True,
    # )
    # return jsonify(success=True)
    processTest = subprocess.Popen(
        ["python3", "-u", "./practiceTest.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # sys.stdout.flush()
    return jsonify(success=True)


# i = 0


@app.route("/stream")
def stream():
    # global i
    # i += 1

    def event_stream():
        # yield f"data: {i}\n\n"
        # return
        # try:
        global processTest
        if processTest:
            # print("HIIIIII")
            # sys.stdout.flush()
            while True:
                output = processTest.stdout.readline()
                if output == "" and processTest.poll() is not None:
                    break
                if output:
                    # print(output)
                    yield f"data: {output}\n\n"
                    # time.sleep(1)
            # print(output)
            # sys.stdout.flush()
            # while output:
            #     yield f"data: {output}\n\n"
            #     time.sleep(1)
        # except Exception as e:
        #     print(f"Error in event_stream: {e}")

    return Response(event_stream(), mimetype="text/event-stream")


@app.route("/stop_test", methods=["POST"])
def stop_test():
    # global process
    global processTest
    # if process and process.returncode is None:
    processTest.terminate()
    return jsonify(success=True)


@app.route("/run-script")
def run_script():
    # Replace 'your_script.py' with the path to your python3 script
    script_path = "./inference_classifier.py"

    # Execute the python3 script using subprocess
    subprocess.run(
        ["python3", script_path], capture_output=False, text=False, check=False
    )


@app.route("/practice")
def practice():
    # data = request.get_json()
    # print(data)
    script_path = "./inference_classifier.py"
    return render_template("practice.html")


# @app.route('/stream')
# def stream():
#     return sse(sse_id='stream', retry=1000)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
