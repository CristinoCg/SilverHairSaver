from django.urls import include, path
from .views import HomePageView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
]