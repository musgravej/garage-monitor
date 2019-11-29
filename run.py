from app import app
import requests
import time
import threading


def initialize_app():
    def start_app():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://192.168.2.53:5000/')
                if r.status_code == 200:
                    print('App started, quiting start_app')
                    not_started = False
                print(r.status_code)
            except requests.exceptions.ConnectionError:
                print('Monitor not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_app)
    thread.start()


if __name__ == '__main__':
    # Set configurations, add to deployment exception list
    # Home config (Ubuntu)
    initialize_app()
    app.run(host='192.168.2.53', port=5000, threaded=True)
