from importlib.resources import Resource
from django.shortcuts import get_object_or_404, render
from .models import Garden, GardenType, Plant
from django.urls import reverse_lazy
##from .forms import ADD FORM NAMES HERE
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'garden/index.html')

def gardens(request):
    garden_list=Garden.objects.all()
    return render(request, 'garden/gardens.html', {'garden_list': garden_list})