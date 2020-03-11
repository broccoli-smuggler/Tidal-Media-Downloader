import flask
from flask import request
from flask import make_response
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


def start(on_login_callback=None):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            sucess = False
            if on_login_callback:
                sucess = on_login_callback(request.data)
            return make_response(str(sucess))
        if request.method == 'GET':
            pass

    app.run()
