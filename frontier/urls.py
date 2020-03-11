from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='frontier-index')
]



