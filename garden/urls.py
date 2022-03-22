from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('gardens/',views.gardens, name='gardens'),
    path('gardenview/<int:id>', views.plants, name='gardenview'),
    path('newgarden/', views.newGarden, name='newgarden'),
    path('newplant/', views.newPlant, name='newplant'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('plantview/<int:id>', views.plantview, name='plantview'),
    #path('plants/<int:id>', views.plants, name='gardenview'),
 
]
