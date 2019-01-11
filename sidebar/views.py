from django.shortcuts import render
from astmodels.models import Users

# Create your views here.

def groups(request):
    #Users.objects.using('asterisk').filter()
    return JsonResponse({}, safe=False)

def extension(request):
    return JsonResponse({}, safe=False)
