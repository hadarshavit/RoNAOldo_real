"""
A sample showing how to make a Python script as an app.
"""
import sys
print(sys.path)
# sys.path = sys.path[2: ]
sys.path.remove('C:\\Users\\Hadar\\Downloads\\pynaoqi-python2.7-2.8.7.4-win64-vs2015-20210818_210634\\pynaoqi-python2.7-2.8.7.4-win64-vs2015-20210818_210634\\lib')
sys.path.append('C:\Users\Hadar\Downloads\pynaoqi-python2.7-2.1.4.13-win32-vs2010\pynaoqi-python2.7-2.1.4.13-win32-vs2010')
sys.path.append(' ')
sys.path.append(r'C:\Users\Hadar\Downloads\robot-jumpstarter-python3-master\robot-jumpstarter-python3-master\python27\stk')
print(sys.path)
import naoqi
__version__ = "0.0.8"

__copyright__ = "Copyright 2020, Jan de Wit, Tilburg University. Robot-jumpstarter project copyright 2015, Aldebaran Robotics"
__author__ = 'Jan de Wit'
__email__ = 'J.M.S.deWit@uvt.nl'

import stk
import stk.runner
import stk.events
import stk.services
import stk.logging

from socket_connection import SocketConnection

class QiConnection(object):
    APP_ID = "com.aldebaran.python27naoqi"
    def __init__(self, qiapp):
        self.qiapp = qiapp
        self.events = stk.events.EventHelper(qiapp.session)
        self.s = stk.services.ServiceCache(qiapp.session)
        #self.logger = stk.logging.get_logger(qiapp.session, self.APP_ID)

        # Set up the socket
        self.socket_server = SocketConnection("python27naoqi", "", 6686, self.message_received)
        self.socket_server.start()

    def message_received(self, origin, message):
        print "Message received from " + origin + ": " + message
        exec(message)

    # For event callbacks
    def __getattr__(self, functionname):
        # print(functionname)

        def wrapper(*args, **kw):
            # print("wrapper called")
            # print('called with %r and %r' % (args, kw))
            argstr = list()

            for a in args:
                if isinstance(a, str):
                    argstr.append('"' + str(a) + '"')
                else:
                    argstr.append(str(a))

            print("Sending message...: " + "python27naoqi:event:" + functionname + "(" + ','.join(argstr) + ")")
            self.socket_server.send("python27", "event:" + functionname + ":" + ','.join(argstr))
            # return getattr(self.child, attr)(*args, **kw)
        return wrapper

    def on_event(self, event):
        pass

    def on_start(self):
        pass

    def stop(self):
        "Standard way of stopping the application."
        self.qiapp.stop()

    def on_stop(self):
        "Cleanup"
        #self.logger.info("Application finished.")
        self.events.clear()

if __name__ == "__main__":
    stk.runner.run_activity(QiConnection)
