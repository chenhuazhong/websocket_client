from ws4py.client.threadedclient import WebSocketClient

class DummyClient(WebSocketClient):
    def opened(self):
        self.send(123)

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, m):
        print (m)
        if len(m) == 175:
            self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = DummyClient('ws://123.207.136.134:9010/ajaxchattest')
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()


