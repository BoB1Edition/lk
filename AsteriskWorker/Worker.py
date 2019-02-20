import asyncio
from asterisk.ami import SimpleAction, AMIClient, EventListener
from lk import settings
import json
import requests
import time
from pymemcache import Client
from pymemcache.client.hash import HashClient


class Worker(object):

    events = []
    PBXClient = None

    def waitEvent(self, timewait = 5):
        while not self.events:
            timewait -= 1
            if timewait == 0:
                break
            time.sleep(1)


    def QueryStat(self):
        self.PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
        self.PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
        secret=settings.JSON_SETTINGS['AMIPassword'])
        self.events = []
        action = SimpleAction(
        'QueueStatus',
        )
        #print('hi')
        self.PBXClient.add_event_listener(self.listener, white_list=['QueueParams'])
        #self.events = ['QueryStat']
        self.PBXClient.send_action(action)
        self.waitEvent()
        self.PBXClient.logoff()
        return self.events

    def QueueAgent(self, Queue):
        self.PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
        self.PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
        secret=settings.JSON_SETTINGS['AMIPassword'])
        self.events = []
        action = SimpleAction(
        'QueueStatus',
        )
        #print('hi')
        #print("Queue: %s" % Queue)
        #q = "'%s'" % Queue
        #print(q)

        self.PBXClient.add_event_listener(self.listener, white_list=['QueueMember'], Queue='%s' % Queue)
        #self.events = ['QueryStat']
        self.PBXClient.send_action(action)
        self.waitEvent()
        self.PBXClient.logoff()
        return self.events

    def Queue(self):
        self.PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
        self.PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
        secret=settings.JSON_SETTINGS['AMIPassword'])
        self.events = []
        action = SimpleAction(
        'Queues',
        )
        #print('hi')
        self.PBXClient.add_event_listener(self.listener)
        #self.events = ['QueryStat']
        ans = self.PBXClient.send_action(action)
        self.waitEvent()
        self.PBXClient.logoff()
        return (self.events, ans)


    def GetQuery(self):
        servers = settings.JSON_SETTINGS['MemcachedServers']
        cServers = []
        for server in servers:
            tmp = server.split(':')
            cServers += [(tmp[0], int(tmp[1]))]
        cl = HashClient(cServers)
        q = cl.get('queue')
        if q is None:
            self.QueryStat()
            queue = []
            for event in self.events:
                queue += [event['Queue']]
            cl.set('queue', ','.join(queue), settings.JSON_SETTINGS['MemcachedExpire'])
            return queue
        else:
            return q.decode("utf-8").split(',')

    def listener(self, event, **kwargs):
        #print(event)
        self.events += [event]

    def __del__(self):
        #print("__del__")
        if not self.PBXClient is None:
            self.PBXClient.logoff()
        #Thread.__del__(self)
