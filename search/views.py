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
    rec = ''
    for qnumber in qnumbers:
        #print('qnumber: %s' % qnumber)
        quniqs = Cel.objects.using('asteriskcdrdb').filter(
        Q(uniqueid=qnumber['uniqueid'])
        ).values('linkedid').distinct()
        for quniq in quniqs:
            #print('quniq: %s' % quniq)
            if quniq['linkedid'] in linkedids:
                continue
            linkedids += [quniq['linkedid']]
    rec = ''
    for linkedid in linkedids:
        #print('linkedid: %s' % linkedid)
        events =  Cel.objects.using('asteriskcdrdb').filter(
        Q(linkedid=linkedid)
        ).values().distinct()
        call = []

        for event in events:
            #print('event: %s' % event)
            if event['exten'] == 'recordcheck':
                rec = '%s' % event['appdata']
                continue
            if event['context']  == 'from-queue' or event['eventtype'] == 'BLINDTRANSFER':
                continue
            if event['eventtype'] == 'CHAN_END' or event['eventtype'] == 'BRIDGE_ENTER'  or event['eventtype'] == 'BRIDGE_EXIT':
                continue
            if event['eventtype'] == 'APP_END':
                continue
            if ((event['context'] == 'from-internal' or event['context'] == 'ext-local') and event['eventtype'] == 'HANGUP'):
                continue
            if event['cid_num'] == '' or event['cid_num'] is None  or event['exten'] == '':
                continue
            if event['eventtype'] == 'ATTENDEDTRANSFER' or event['eventtype'] == 'LOCAL_OPTIMIZE':
                continue
            call += [{
            'date': event['eventtime'],
            'text': eventToText(event),
            'linkedid' : event['linkedid'],
            'uniqueid' : event['uniqueid'],
            }]
            #print(event['eventtime'])
        calls += [{
        'calls': call,
        'rec' : (rec.split(','))[0]
        }]
# print(calls)
    return render(request, 'search/result.html', {'calls':calls})

def eventToText(event):
    pattern = re.compile("ivr-(.*)")
    text = ''
    if event['eventtype'] == 'CHAN_START':
        if event['context'] == 'from-internal':
            text = "Звоним на номер %s" % (event['cid_num'])
        else:
            text = "Звонок с номера %s на номер %s начался" % (event['cid_num'], event['exten'])
    elif event['eventtype'] == 'LINKEDID_END':
        text = "Звонок с номера %s на номер %s завершен" % (event['cid_num'], event['exten'])
    elif event['eventtype'] == 'ANSWER':
        if pattern.match(event['context']):
            ivr = IvrDetails.objects.using('asterisk').filter(
            id=pattern.match(event['context'])[1]
            ).values('name')
            text = "Запустилось приветствие %s" % ivr[0]['name']
        else:
            text = "Ответил %s" % event['cid_num']
    elif event['eventtype'] == 'APP_START':
        if event['context'] == 'ext-queues':
            text = 'Переведен в очередь %s' % event['exten']
    elif event['eventtype'] == 'HANGUP':
        text = 'Абонент %s положил трубку' % event['cid_num']
    else:
        text = '%s' % event
    return text
