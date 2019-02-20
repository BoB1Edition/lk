from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from lk import settings
from asterisk.ami import SimpleAction, AMIClient
from lkview.models import Cdr, Astdb
from django.db.models import Q
import re, os
from astmodels.models import *
from AsteriskWorker import *

@login_required
def index(request):
    w = Worker()
    regrecord = re.compile("record-(\d{4})", re.IGNORECASE|re.UNICODE)
    liitem = {}
    queue = w.GetQuery()
    for gr in request.user.groups.all():
        try:
            if not regrecord.match('%s' % gr.name) is None:
                t = regrecord.match('%s' % gr.name)[1]
                print("t: %s" % t)
                value = '%s' % t

                if value in queue:
                    key = QueuesConfig.objects.using('asterisk').filter(
                    extension = ('%s' % value)).values_list('descr').get()[0]
                else:
                    key = Users.objects.using('asterisk').filter(
                    extension = ('%s' % value)).values_list('name').get()[0]

                print("users key: %s\nvalue: %s" % (key, value))
                liitem[key] = value
        except Exception as e:
            print(e)
            continue
    mynumber = request.user.aduser.telephoneNumber
    l=[]
    for i, j in sorted(liitem.items(), key=lambda x: x[0].lower()): l+= [(i, j)]
    context = {'liitem': l, 'mynumber' : mynumber}
    return render(request, 'lkview/index.html', context)

@login_required
def mainjs(request):
    return render(request, 'lkview/js/main.js', {
    'mynumber' : request.user.aduser.telephoneNumber
    }, content_type='application/javascript')

def number(request, num):
    print('num: %s' % num)
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
