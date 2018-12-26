from threading import Thread
from asterisk.ami import SimpleAction, AMIClient
from lk import settings
from queue import Queue
import datetime, time


class Worker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
        self.PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
        secret=settings.JSON_SETTINGS['AMIPassword'])
        self.PBXClient.add_event_listener(self.listener)
        self.setDaemon(True)
        self.start()


    def run(self):
        while True:
            action = SimpleAction('ping')
            self.PBXClient.send_action(action)
            if self.queue.qsize() == 0:
                time.sleep(60)
                continue
            action = self.queue.get()
            print(
            self.PBXClient.send_action(action).response
            )
            print('Time: %s' % datetime.datetime.now())

    def listener(self, event, **kwargs):
        pass
        #print(event)
        #def internallistener(event, **kwargs):
        #    print(event)
        #return internallistener
    def __del__(self):
        print("__del__")
        PBXClient.logoff()
        Thread.__del__(self)
