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

# Create your views here.

@login_required
def BlackAster(request):
    r = re.compile(r"rec.*-(\d+)")
    numbers = []
    for gr in request.user.aduser.groups.values_list('groupname'):
        try:
            q = r.match(gr[0])[1]
            qset = Astdb.objects.using('astdb').filter(key__contains='/QPENALTY/%s/agents' % q)
            if qset.count() > 0:
                for agent in qset:
                    numbers += ['%s' % agent.key.split('/')[-1]]
            else:
                numbers += ['%s' % q]
        except Exception as e:
            pass
    numbers.sort()
    content = {
    'numbers' : numbers,
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
    time.sleep(25)
    PBXClient.logoff()
    return HttpResponse(ans.response)

@login_required
def sipphone(request):
    content = {'server': settings.JSON_SETTINGS['asteriskServer'],
    'password' : '3da4cfd14733c57baf77012eab1569c6'}
    return render(request, 'js/sipphone.js', content)
