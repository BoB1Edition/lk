from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from threading import Thread
from django.http import HttpResponse, JsonResponse
from asterisk.ami import SimpleAction, AMIClient, EventListener
from lkview.models import *
from lk import settings
from threading import Lock
import time, re
from AsteriskWorker import Worker

# Create your views here.

@login_required
def BlackAster(request):
    w = Worker()
    queues = w.GetQuery()
    print('queues: %s\n' % queues)
    r = re.compile(r"rec.*-(\d+)")
    numbers = []
    for gr in request.user.aduser.groups.values_list('groupname'):
        try:
            q = r.match(gr[0])[1]
            # qset = Astdb.objects.using('astdb').filter(key__contains='/QPENALTY/%s/agents' % q)
            
            if q in queues:
                print('if q: %s' % q)
                qset = QueuesConfig.objects.using('asterisk').filter(extension = ('%s' % q)).values_list('descr')
                print(qset)
                for agent in qset:
                    numbers += ['%s' % agent.key.split('/')[-1]]
            else:
                print('else q: %s' % q)
                numbers += ['%s' % q]
        except Exception as e:
            pass
    numbers.sort()
    fio = []
    content = {
    'numbers' : numbers,
    'fio': fio
    }
    return render(request, 'blackaster/main.html', content)

@login_required
def BlackMainJS(request):
    return render(request, 'blackaster/js/main.js')

@login_required
def Listen(request, num):
    print(request.user.aduser.telephoneNumber)
    PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
    PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
    secret=settings.JSON_SETTINGS['AMIPassword'])
    print(PBXClient)
    action = SimpleAction('Originate',
    Channel = ('SIP/%s' % request.user.aduser.telephoneNumber),
    CallerID = ('Spy%s' % num),
    #Exten = '6670',
    #Application = 'Playback',
    Application = 'ChanSpy',
    #Data = '/var/spool/asterisk/monitor/2017/10/03/out-1694-6666-20171003-103712-1507016232.189',
    Data = ('SIP/%s,qx' % num),
    Timeout = '30000',
    #Priority = '1',
    #Async = 'yes'
    )
    print(action)
    ans = PBXClient.send_action(action)
    print(ans.response)
    PBXClient.logoff()
    return HttpResponse(ans.response)

def test(request):
    w = Worker()
    events = w.GetQuery()
    print(events)
    return HttpResponse(events)
