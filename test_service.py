# -*- coding: utf-8 -*-

# CONFIG
SERVER_HOSTNAME = 'localhost'
SERVER_PORT = 6809
SERVICE_NAME = 'TestService'
SERVICE_DISPLAY_NAME = 'テストサービス'
SERVICE_DESCRIPTION = 'WindowsサービスをPythonで作ってみた\r\n(説明欄は改行もOK)'


import sys
import os
import os.path
from socketserver import ThreadingMixIn
from wsgiref.simple_server import WSGIServer

import win32service
import win32serviceutil
import win32event

if not sys.stdout:
    sys.stdout = open(os.devnull, 'w')
if not sys.stderr:
    sys.stderr = open(os.devnull, 'w')
import bottle


app = bottle.app()
service_stop_event = win32event.CreateEvent(None, 0, 0, None)


class XWSGIServer(ThreadingMixIn, WSGIServer):

    def service_actions(self):
        r = win32event.WaitForSingleObject(service_stop_event, 0)
        if r == win32event.WAIT_OBJECT_0:
             self._BaseServer__shutdown_request = True


class Service(win32serviceutil.ServiceFramework):

    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = SERVICE_DISPLAY_NAME
    _svc_description_ = SERVICE_DESCRIPTION

    def __init__(self, *args, **kwargs):
        win32serviceutil.ServiceFramework.__init__(self, *args, **kwargs)

    def SvcDoRun(self):
        bottle.run(app=app, host=SERVER_HOSTNAME, port=SERVER_PORT, quiet=True,
                   server_class=XWSGIServer)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(service_stop_event)


def no_cache(callback):
    def wrapper(*args, **kwargs):
        bottle.response.set_header('Pragma', 'no-cache')
        bottle.response.set_header('Cache-Control', 'no-store')
        return callback(*args, **kwargs)
    return wrapper


@app.get('/hello')
@no_cache
def hello_get():
    return 'Hello!'


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Service)
