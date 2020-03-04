import zmq
import threading
import time


class ServerZmq(threading.Thread):
    def __init__(self, port=8000, callback=None, default_response='ack'):
        super(ServerZmq, self).__init__()
        context = zmq.Context()
        self._socket = context.socket(zmq.REP)
        self._socket.bind("tcp://*:%s" % port)
        self._callback = callback
        self._thread_stop = threading.Event()
        self._response = default_response

    def set_callback(self, callback):
        self._callback = callback

    def stop(self):
        self._thread_stop.set()

    def run(self):
        while not self._thread_stop.is_set():
            message = self._socket.recv()
            message = message.decode('ascii')
            print("Received request: %s" % message)

            result = self._response
            if self._callback:
                result = self._callback(message)

            self._socket.send_string(str(result))
            time.sleep(0.05)


class ClientZmq(threading.Thread):
    def __init__(self, port=8000, callback=None):
        super(ClientZmq, self).__init__()
        context = zmq.Context()
        self._socket = context.socket(zmq.REQ)
        self._socket.connect("tcp://localhost:%s" % port)
        self._callback = callback
        self._message = None
        self._thread_stop = threading.Event()

        self.poller = zmq.Poller()
        self.poller.register(self._socket, zmq.POLLIN)

    def set_callback(self, callback):
        self._callback = callback

    def send_message(self, message):
        self._message = str(message)

    def stop(self):
        self._thread_stop.set()

    def run(self):
        while not self._thread_stop.is_set():
            if self._message:
                self._socket.send_string(self._message)
                expect_reply = True
                while expect_reply:
                    socks = dict(self.poller.poll(3000))
                    if socks.get(self._socket) == zmq.POLLIN:
                        response = self._socket.recv()
                        response = response.decode('ascii')
                        print("Received request: %s" % response)
                        if self._callback:
                            self._callback(response)
                    else:
                        print("No response, dropping message %s" % self._message)
                    expect_reply = False
                self._message = None
            else:
                time.sleep(0.05)
