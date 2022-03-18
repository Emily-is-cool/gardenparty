from importlib.resources import Resource
from django.shortcuts import get_object_or_404, render
from .models import Garden, GardenType, Plant
from django.urls import reverse_lazy, reverse
from .forms import GardenForm, PlantForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'garden/index.html')

def gardens(request):
    garden_list=Garden.objects.all()
    return render(request, 'garden/gardens.html', {'garden_list': garden_list})

def gardenview(request, id):
    gardenview=Garden.objects.all()
    return render(request, 'garden/gardenview.html', {'gardenview': gardenview})

@login_required
def newGarden(request):
    if request.method=='POST':
        form = GardenForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=GardenForm()
    else:
        form=GardenForm()
    return render(request, 'garden/newgarden.html', {'form': form})

@login_required
def newPlant(request):
    if request.method=='POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=PlantForm()
    else:
        form=PlantForm()
    return render(request, 'garden/newplant.html', {'form': form})

def loginmessage(request):
    return render(request, 'garden/loginmessage.html')

def logoutmessage(request):
    return render(request, 'garden/logoutmessage.html')