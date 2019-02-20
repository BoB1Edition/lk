from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from threading import Thread
from django.http import HttpResponse, JsonResponse
from AsteriskWorker import *
from checkquery.models import *
from lkview.models import *
from lk import settings
from threading import Lock
import time, re

# Create your views here.

@login_required
def checkqueryMain(request):
    r = re.compile(r"rec.*-(\d+)")
    w = Worker()
    allqueues = w.GetQuery()
    queues = []
    for gr in request.user.aduser.groups.values_list('groupname'):
        #print("gr: %s" % gr)
        try:
            qnum = r.match(gr[0])
            #print("qnum: %s" % qnum[1])
            if (not qnum is None) and (qnum[1] in allqueues):
                print("%s: %s" % (qnum[1] in allqueues, qnum[1]))
                qset = QueuesConfig.objects.using('asterisk').filter(
                extension = qnum[1]
                )
                if qset.count() > 0:
                    queues += [qset.values_list('descr', 'extension').get()]
        except Exception as e:
            print(e)
            pass
    l=[]
    for i, j in sorted(queues, key=lambda x: x[0].lower()): l+= [(i, j)]
    content = {
    'queues' : l,
    }
    return render(request, 'checkquery/main.html', content)

@login_required
def MainJS(request):
    return render(request, 'checkquery/js/main.js')

@login_required
def queue(request, num):
    r = re.compile(r'.*\D(?P<num>\d{4,5})\D.+')
    w = Worker()
    #print("num: %s" % num)
    Agents = w.QueueAgent('%s' % num)
    AgentsIn = []
    for Agent in Agents:
        nums = r.match(Agent['Location'])['num']
        paused = Agent['Paused']
        fio = Agent['Name']
        AgentsIn += [{'nums': nums, 'paused' : paused, 'fio' : fio}]
        #print('nums: %s, paused: %s, fio: %s' % (nums, paused, fio))
    content = {'Queue' : num, 'AgentsIn' : AgentsIn}
    print(content)
    return render(request, 'checkquery/result.html', content)
