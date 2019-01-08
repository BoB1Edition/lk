from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from lk import settings
import time, re, json, datetime
from django.db.models import Q
from reportvpn.models import *

# Create your views here.

def reportvpnMain(request):
    return render(request, 'reportvpn/main.html')

def reportvpnMainJS(request):
    return render(request, 'reportvpn/js/main.js')

def reportvpnMainReport(request):
    json_data = json.loads(request.body)
    conections = Connections.objects.using('vpn').filter(
    user__icontains=json_data['Login']
    )
    if json_data['databegin'] != "" and json_data['dataend'] != "":
        conections = conections.filter(timestamp__range = (json_data['databegin'], json_data['dataend']))
    elif json_data['databegin'] != "":
        conections = conections.filter(timestamp__gte = json_data['databegin'])
    elif json_data['dataend'] != "":
        conections = conections.filter(timestamp__lte = json_data['dataend'])
    pairs = []
    connect = None
    worktime = datetime.timedelta()
    for conection in conections:
        if conection.status == 'started':
            connect = conection
        if conection.status == 'terminated' and connect != None:
            pairs += [
            {'login': connect.user,
            'started': connect.timestamp,
            'terminated': conection.timestamp,
            'difference': '%s' % (conection.timestamp - connect.timestamp)
            }
            ]
            worktime += conection.timestamp - connect.timestamp
            connect = None
    print(worktime)
    return render(request, 'reportvpn/result.html', {'pairs': pairs, 'worktime': worktime})
