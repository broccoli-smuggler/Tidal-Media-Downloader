import tidal_dl
import time
from zmq_helper import ServerZmq


class Server(object):
    def __init__(self):
        self.zmq_server = ServerZmq(callback=self.on_request)
        self.zmq_server.start()

    def cleanup(self):
        self.zmq_server.stop()

    def parse_request(self, request):
        message = request.split(';')
        header = message[0]
        return header, message[1:]

    def login(self, payload):
        print("LOGIN")
        username, password = payload
        return tidal_dl.log_in(username, password)

    def on_request(self, request):
        request, payload = self.parse_request(request)
        if request == 'login':
            return str(self.login(payload))
        return 'ack'


if __name__ == '__main__':
    s = Server()

    running = True
    while running:
        try:
            time.sleep(1)
        except (KeyboardInterrupt, SystemError) as e:
            running = False
            s.cleanup()
            print('fin')
            raise e
