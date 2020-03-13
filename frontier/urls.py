from django.urls import path
from . import views
from .views import create_aa, show_aa, ChartData

urlpatterns = [
    path('new', create_aa, name='create_aa'),
    path('api/chart/data/', ChartData.as_view(), name='chart_data'),
    path('<int:id>/', show_aa, name='show_aa')
]



