from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from lk import settings
from asterisk.ami import SimpleAction, AMIClient
from lkview.models import Cdr, Astdb
from django.db.models import Q
import re, os
from subprocess import Popen

@login_required
def index(request):
    #PBXClient = AMIClient(address=settings.JSON_SETTINGS['asteriskServer'],port=5038)
    #PBXClient.login(username=settings.JSON_SETTINGS['AMILogin'],
    #secret=settings.JSON_SETTINGS['AMIPassword'])
    #def event_listener(event,**kwargs):
    #    print(event)

    #PBXClient.add_event_listener(event_listener, white_list=['DBGetResponse'])
    #action = SimpleAction(
    #'Logoff',
    #Queue='1990',
    #Interface='sip/6328',
    #Penalty=1,
    #Paused='false'
    #)
    #print()
    # PBXClient = settings.PBXClient
    #ans = PBXClient.send_action(action, callback=callback_response)
    #print(ans)
#    action = SimpleAction('Originate',
#    Channel='SIP/6350',
#    Exten='6633',
#    Priority=1,
#    Context='default',
#    CallerID='python',
#    )
#    ans = PBXClient.send_action(action, callback=callback_response)
    regrecord = re.compile("record-(\d{4})", re.IGNORECASE|re.UNICODE)
    liitem = []
    for gr in request.user.groups.all():
        try:
            t = regrecord.match('%s' % gr.name)[1]

            queue = Astdb.objects.using('astdb').filter(key__contains='/QPENALTY/%s/agents' % t)
            if queue.count() > 0:
                for agent in queue:
                    liitem = addnotdouble(['%s' % agent.key.split('/')[-1]], liitem)
            else:
                liitem = addnotdouble(['%s' % t], liitem)
        except Exception as e:
            print(e)
            continue
    #Astdb.objects.using('astdb').filter(key__contains='/QPENALTY/%s/agents' % )
    mynumber = request.user.aduser.telephoneNumber
    #liitem += ['0000']
    # print("response: %s" % ans.response)
    liitem.sort()
    context = {'liitem': liitem, 'mynumber' : mynumber}
    #return HttpResponse('%s' % dir(request.user))
    return render(request, 'lkview/index.html', context)

def callback_response(response):
    print(response)

def addnotdouble(item, items):
    items.sort()
    print(item)
    if item[0] not in items:
        print('if')
        items += item
    else:
        print(items)

    return items

@login_required
def mainjs(request):
    return render(request, 'lkview/js/main.js', {
    'mynumber' : request.user.aduser.telephoneNumber
    }, content_type='application/javascript')

def number(request, num):
    print(number)
    r = re.compile('.*-(.+)-(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})(\d{2})-.*')
    recordingfiles = Cdr.objects.using('asteriskcdrdb').filter(
    ~Q(recordingfile = ''),
    dst = ('%s' % num),
    disposition='ANSWERED'
    ).order_by('-calldate').values_list('recordingfile', flat=True).distinct()
    rfs = [y for y in recordingfiles]
    dt = []
    for rf in rfs:
        filename = 'resource/%s/%s/%s/%s' % (r.match(rf)[2], r.match(rf)[3],
        r.match(rf)[4], r.match(rf)[0])
        if not os.path.isfile(filename):
            continue
        dt += [{'data' : '%s/%s/%s %s:%s:%s' % (r.match(rf)[2], r.match(rf)[3],
        r.match(rf)[4], r.match(rf)[5], r.match(rf)[6], r.match(rf)[7]),
        'extern' : '%s' % r.match(rf)[1],
        'filename' : '/%s' % filename,
        'direction': 'in',
        }]
    recordingfiles = Cdr.objects.using('asteriskcdrdb').filter(
    ~Q(recordingfile = ''),
    cnum = ('%s' % num),
    disposition='ANSWERED'
    ).order_by('-calldate').values_list('recordingfile', flat=True).distinct()[0:20]
    rfs = [y for y in recordingfiles]
    r = re.compile('.+-(\d*)-\d+-(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})(\d{2}).*')
    for rf in rfs:
        filename = 'resource/%s/%s/%s/%s' % (r.match(rf)[2], r.match(rf)[3],
        r.match(rf)[4], r.match(rf)[0])
        if not os.path.isfile(filename):
            continue
        dt += [{'data' : '%s/%s/%s %s:%s:%s' % (r.match(rf)[2], r.match(rf)[3],
        r.match(rf)[4], r.match(rf)[5], r.match(rf)[6], r.match(rf)[7]),
        'extern' : '%s' % r.match(rf)[1],
        'filename' : '/%s' % filename,
        'direction': 'out',
        }]
    print(dt)
    return JsonResponse(dt, safe=False)

def convert(request, fname):
    #os.process('ffmpeg -i %s -acodec libvorbis output.ogg')
    output = fname.split('/')[-1][:-3]
    if os.path.isfile('convert/%sogg' % output):
        return JsonResponse({})

    cmd = 'ffmpeg -i %s -acodec libvorbis convert/%sogg' % (fname, output)
    #p = Popen(['ffmpeg', '-i', fname, '-acodec', 'libvorbis', 'convert/%sogg' % output])
    os.system(cmd)
    cmd = 'find convert/ -type f -mmin +360 -delete'
    os.system(cmd)
    return JsonResponse({})

@login_required
def main(request):
    content = {'is_vpn' : False}
    for gr in request.user.groups.values('name'):
        if gr['name'] == 'vpn-report':
            print('name')
            content = {'is_vpn' : True}
        else:
            print('else: ',gr['name'])
    return render(request, 'lkview/main.html', content)
