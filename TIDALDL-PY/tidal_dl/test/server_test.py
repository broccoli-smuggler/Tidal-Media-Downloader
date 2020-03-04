import unittest
import time
from .. import server
from .. import zmq_helper


class SeverTest(unittest.TestCase):
    def __client_callback(self, response):
        self.c_ack = response
        self.received = True

    def setUp(self):
        self.c_ack = None
        self.received = False
        self.server = server.Server()

        self.client = zmq_helper.ClientZmq(callback=self.__client_callback)
        self.client.start()

    def test_something(self):
        self.client.send_message('login;poo;poos')
        while not self.received:
            time.sleep(0.1)

        self.assertEqual(self.c_ack, 'login')


if __name__ == '__main__':
    unittest.main()
