from django.shortcuts import render, redirect
from .models import AssetClass
from .models import Allocation
from .forms import AllocationForm

from .eff_front import efficient_frontier

from rest_framework.views import APIView
from rest_framework.response import Response

def create_aa(request):
    form = AllocationForm(request.POST or None)
    
    if form.is_valid():
        allocation_obj = form.save()
        return redirect('show_aa', id=allocation_obj.id)

    asset_classes = AssetClass.objects.all()
    return render(request, 'frontier/new-form.html', {'asset_classes': asset_classes, 'form': form})


def show_aa(request, id):
    allocation = Allocation.objects.get(id=id)
    return render(request, 'frontier/show.html', {'allocation': allocation})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        aa_id = request.GET['aa_id']
        allocations = Allocation.objects.get(id=aa_id)
        data = efficient_frontier(allocations)
        content = {
            'data': data
        }
        return Response(content)