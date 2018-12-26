from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from threading import Thread
from django.http import HttpResponse, JsonResponse
from asterisk.ami import SimpleAction, AMIClient, EventListener
from checkquery.models import *
from lkview.models import *
from lk import settings
from threading import Lock
import time, re

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

@login_required
def queue(request, num):
    r = re.compile(r'.*/(\d+).*;(\d);(.*);')
    qset = Astdb.objects.using('astdb').filter(key='/Queue/PersistentMembers/%s' % num).values('value')
    AgentsIn = []
    for q in qset:
        agents = q['value'].split('|')
        #print(agents)
        for agent in agents:
            nums = r.match(agent)[1]
            paused = r.match(agent)[2]
            fio = r.match(agent)[3]
            AgentsIn += [{'nums': nums, 'paused' : paused, 'fio' : fio}]
            #print('nums: %s, paused: %s, fio: %s' % (nums, paused, fio))
    content = {'Queue' : num, 'AgentsIn' : AgentsIn}
    print(content)
    return render(request, 'checkquery/result.html', content)
