from django.urls import include, path
from .views import HomePageView

urlpatterns=[
    path('', HomePageView, name='home'),
]