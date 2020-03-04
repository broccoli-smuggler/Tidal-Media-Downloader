import unittest
from .. import zmq_helper
import time


class ClientServerTest(unittest.TestCase):
    def __callback_client(self, response):
        self.ack_c = response

    def __calback_server(self, request):
        self.ack_s = request
        return "ack"

    def setUp(self):
        self.ack_c = None
        self.ack_s = None
        self.client = zmq_helper.ClientZmq(callback=self.__callback_client)
        self.server = zmq_helper.ServerZmq(callback=self.__calback_server)
        self.client.start()
        self.server.start()

    def tearDown(self):
        self.client.stop()
        self.server.stop()

    def test_end_to_end(self):
        self.client.send_message("Hello world")
        time.sleep(0.1)

        self.assertEqual(self.ack_s, "Hello world")
        self.assertEqual(self.ack_c, "ack")

        self.client.send_message(4)
        time.sleep(0.1)

        self.assertEqual(self.ack_s, "4")
        self.assertEqual(self.ack_c, "ack")

        self.client.stop()
        self.server.stop()


if __name__ == '__main__':
    unittest.main()
