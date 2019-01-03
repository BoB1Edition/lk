from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from lk import settings
import time, re

# Create your views here.

def reportvpnMain(request):
    return render(request, 'reportvpn/main.html')

def reportvpnMainJS(request):
    return render(request, 'reportvpn/js/main.js')

def reportvpnMainReport(request):
    print(request.body)
    return render(request, 'reportvpn/result.html')
