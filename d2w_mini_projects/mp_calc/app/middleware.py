import os
import socket

class PrefixMiddleware(object):

    def __init__(self, app, voc=True):
        self.app = app
        if voc:
            self.prefix = f'/proxy/5000/'
        else:
            self.prefix = ''

    def __call__(self, environ, start_response):
        print(environ['PATH_INFO'], self.prefix)
        environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)

    def get_myip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        return s.getsockname()[0]