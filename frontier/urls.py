from django.urls import path
from . import views
from .views import create_aa, show_aa

urlpatterns = [
    path('new', create_aa, name='create_aa'),
    path('<int:id>', show_aa, name='show_aa')
]



