from django.shortcuts import render
from .models import AssetClass

def index(request):
    context = {
        'asset_classes': AssetClass.objects.all()
    }
    return render(request, 'frontier/index.html', context)