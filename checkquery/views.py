from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from threading import Thread
from django.http import HttpResponse, JsonResponse
from asterisk.ami import SimpleAction, AMIClient, EventListener
from checkquery.models import *
from lk import settings
from threading import Lock
import time, re

mutex = Lock()
Events = []
# Create your views here.

class CEvents(EventListener):
    def on_event(event,**kwargs):
        print('Event',event)

    def on_Registry(event,**kwargs):
        print('Registry Event',event)

@login_required
def checkqueryMain(request):
    r = re.compile(r"rec.*-(\d+)")
    queues = []
    for gr in request.user.aduser.groups.values_list('groupname'):
        try:
            q = r.match(gr[0])[1]
            qset = QueuesConfig.objects.using('asterisk').filter(
            extension = q
            )
            if qset.count() > 0:
                queues += [q]
        except Exception as e:
            pass
        content = {
        'queues' : queues,
        }
    return render(request, 'checkquery/main.html', content)

@login_required
def MainJS(request):
    return render(request, 'checkquery/js/main.js')

def queue(request, num):
    PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
    PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
    secret=settings.JSON_SETTINGS['AMIPassword'])
    PBXClient.add_event_listener(listener(request), white_list=['QueueMember', 'QueueStatusComplete'])
    PBXClient.add_event_listener(CEvents, white_list=['QueueMember', 'QueueStatusComplete'])
    action = SimpleAction('QueueStatus')
    PBXClient.send_action(action)
    #while mutex.locked():
    #time.sleep(10)
    #    print(mutex.locked())
    return render(request, 'checkquery/result.html', {'events': Events} )

def listener(request):
    def internallistener(event, **kwargs):
        Events += [event]
    return internallistener
