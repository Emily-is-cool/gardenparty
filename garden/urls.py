from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('gardens/',views.gardens, name='gardens')
]
