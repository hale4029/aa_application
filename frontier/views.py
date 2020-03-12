from django.shortcuts import render, redirect
from .models import AssetClass
from .models import Allocation
from .forms import AllocationForm


def create_aa(request):
    form = AllocationForm(request.POST or None)
    
    if form.is_valid():
        allocation_obj = form.save()
        return redirect('show_aa', id=allocation_obj.id)

    asset_classes = AssetClass.objects.all()
    return render(request, 'frontier/new-form.html', {'asset_classes': asset_classes, 'form': form})


def show_aa(request, id):
    #import pdb; pdb.set_trace()
    allocation = Allocation.objects.get(id=id)
    return render(request, 'frontier/show.html', {'allocation': allocation})
