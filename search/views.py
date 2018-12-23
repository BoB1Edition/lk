from django.shortcuts import render
from search.forms import FindForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from search.models import *
from django.db.models import Q
import json, re

# Create your views here.

@login_required
def searchMain(request):
    return render(request, 'search/main.html')

@login_required
def autoFill(request):
    return render(request, 'search/js/autofill.js')

def autocomplete(request):
    query = request.GET.get('query', '')
    print('query: %s' % query)
    qnumbers = Cdr.objects.using('asteriskcdrdb').filter(
    Q(src__contains=query) | Q(dst__contains=query) | Q(cnum__contains=query)
    ).order_by('-calldate').values('src', 'dst', 'cnum', 'uniqueid')
    numbers = set([x['src'] for x in qnumbers])
    number = []
    i = 1
    print('qnumbers: %s' % qnumbers)
    for qnumber in numbers:
        number += [{'id' : i, 'name' : qnumber}]
        i += 1
    print(number)
    return JsonResponse(number, safe=False)

def result(request, num):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    qnumbers = Cdr.objects.using('asteriskcdrdb').filter(
    (Q(src__contains=num) | Q(dst__contains=num) | Q(cnum__contains=num)) &
    Q(calldate__range=(body['Before'], body['After']))
    ).order_by('-calldate').values('uniqueid').distinct()
    linkedids = []
    calls = []
    for qnumber in qnumbers:
        #print('qnumber: %s' % qnumber)
        quniqs = Cel.objects.using('asteriskcdrdb').filter(
        Q(uniqueid=qnumber['uniqueid'])
        ).values('linkedid').distinct()
        for quniq in quniqs:
            #print('quniq: %s' % quniq)
            linkedids += [quniq['linkedid']]
            rec = ''
            for linkedid in linkedids:
                #print('linkedid: %s' % linkedid)
                events =  Cel.objects.using('asteriskcdrdb').filter(
                Q(linkedid=linkedid)
                ).values()
                call = []

                for event in events:
                    #print('event: %s' % event)
                    if event['exten'] == 'recordcheck':
                        rec = event['appdata']
                        continue
                    if event['eventtype'] == 'CHAN_END' or event['exten'] == 's':
                        continue
                    if event['cid_num'] == '' or event['cid_num'] is None  or event['exten'] == '':
                        continue
                    call += [{
                    'date':event['eventtime'],
                    'text': eventToText(event),
                    'rec' : 'rec'
                    }]
                calls += [call]
    print(calls)
    return render(request, 'search/result.html', {'calls':calls})

def eventToText(event):
    pattern = re.compile("ivr.*")
    text = ''
    if event['eventtype'] == 'CHAN_START':
        text = "Звонок с номера %s на номер %s начался" % (event['cid_num'], event['exten'])
    elif event['eventtype'] == 'LINKEDID_END':
        text = "Звонок с номера %s на номер %s завершен" % (event['cid_num'], event['exten'])
    elif event['eventtype'] == 'ANSWER':
        if pattern.match(event['context']):
            text = "Запустилось приветствие"
        else:
            text = "Ответил %s" % event['cid_num']
    elif event['eventtype'] == 'APP_START':
        if event['context'] == 'ext-queues':
            text = 'Переведен вочередь %s' % event['exten']
    elif event['eventtype'] == 'HANGUP':
        text = 'Абонент %s положил трубку' % event['cid_num']
    else:
        text = '%s' % event
    return text
