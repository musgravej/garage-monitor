from flask import Flask, render_template, url_for, request, g, redirect, flash, make_response, jsonify
import datetime
# import requests
import threading
import time

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.ProductionConfig')


@app.before_first_request
def start_monitor():
    def run_monitor():
        while True:
            print("Run recurring task")
            time.sleep(3)

    thread = threading.Thread(target=run_monitor)
    thread.start()


@app.before_request
def before_request():
    pass


@app.route("/", methods=['GET', 'POST'])
def app_home():
    now = datetime.datetime.now()
    time_string = now.strftime("%m/%d/%Y %I:%M %p")
    page_data = {
        'title': 'Garage Monitor',
        'time': time_string,
        'request': request
    }

    return render_template('main.html', **page_data)


if __name__ == '__main__':
    pass
