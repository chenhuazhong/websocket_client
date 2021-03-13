from ws4py.client.threadedclient import WebSocketClient
from ws4py.messaging import TextMessage

from utils import MessageScrolledText


class DummyClient(WebSocketClient):

    def __init__(self, message: MessageScrolledText, *args, **kwargs):
        self.message = message
        super(DummyClient, self).__init__(*args, **kwargs)

    def opened(self):
        self.send("123")


    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m: TextMessage):
        self.message.INFO(m.data.decode())


def run(ws):
    try:

        ws.connect()
        ws.run_forever()

    except KeyboardInterrupt:
        ws.close()

if __name__ == '__main__':
    try:
        ws = DummyClient('ws://123.207.136.134:9010/ajaxchattest')
        ws.connect()
        ws.send("asdfasdf")
        # ws.run_forever()
        ws._th.join()
    except KeyboardInterrupt:
        ws.close()