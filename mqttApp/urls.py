from django.urls import path
from .views import (
    HomePageView, 
    TemperaturaView, 
    BatimentoView,
    
    LocalizacaoView,
    ClienteView)

urlpatterns=[
    path('', HomePageView, name='home'),
    path('paciente/', ClienteView, name='paciente'),
    
]

broker_ulrpatterns=[
    path('batimento', BatimentoView, name='batimento'),
    path('temperatura', TemperaturaView, name='temperatura'),
    path('localizacao', LocalizacaoView, name='localizacao'),
]
urlpatterns += broker_ulrpatterns