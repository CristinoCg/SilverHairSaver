from django.urls import path
from .views import (
    HomePageView, 
    TemperaturaView, 
    BatimentoView,
    OxigenioView,
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
    path('oxigenio', OxigenioView, name='oxigenio')

]
urlpatterns += broker_ulrpatterns