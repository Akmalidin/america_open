from django.urls import path
from .views import index, packet
urlpatterns = [
    path('', index, name='index'),
    path('packet/<slug:slug>/', packet, name='packet')
    
    
    
]
