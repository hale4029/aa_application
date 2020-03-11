from django.shortcuts import render

def index(request):
    return render(request, 'frontier/index.html', context=None)