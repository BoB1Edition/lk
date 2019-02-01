import asyncio
from asterisk.ami import SimpleAction, AMIClient, EventListener
from lk import settings
import json
import requests
import time
from pymemcache import Client


class Worker(object):

    events = []

    def __init__(self):
        Client()
        self.PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
        self.PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
        secret=settings.JSON_SETTINGS['AMIPassword'])


    def QueryStat(self):
        self.events = []
        action = SimpleAction(
        'QueueStatus',
        )
        #print('hi')
        self.PBXClient.add_event_listener(self.listener, white_list=['QueueParams'])
        #self.events = ['QueryStat']
        self.PBXClient.send_action(action)
        while not self.events:
            #print(self.events)
            time.sleep(1)
            #print('done')
        self.PBXClient.logoff()
        return self.events

    def listener(self, event, **kwargs):
        #print(event)
        self.events += [event]

    def __del__(self):
        print("__del__")
        self.PBXClient.logoff()
        #Thread.__del__(self)
