from django.shortcuts import render

# Create your views here.
def queuestats(request):
    return render(request, 'iframes/queuestats.html')
