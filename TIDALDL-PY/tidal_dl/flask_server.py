import flask
import time
from flask import request
from flask import make_response
from flask_cors import CORS
from zmq_helper import ClientZmq


def start(on_login_callback=None):
    app = flask.Flask(__name__)
    CORS(app)
    app.config["DEBUG"] = True

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            success = False
            if on_login_callback:
                success = on_login_callback(request.data)
            return make_response(str(success))
        if request.method == 'GET':
            pass

    app.run()


if __name__ == '__main__':
    c = ClientZmq()
    c.start()

    def login_callback(data):
        outer_res = None

        def response_callback(res):
            nonlocal outer_res
            outer_res = res

        c.set_callback(response_callback)
        c.send_message(str(data.decode('ascii')))

        # Wait for a response
        while outer_res is None:
            time.sleep(0.01)

        return outer_res


    start(login_callback)

    running = True
    while running:
        try:
            time.sleep(1)
        except (KeyboardInterrupt, SystemError) as e:
            running = False
            c.stop()
            print('fin')
            raise e
