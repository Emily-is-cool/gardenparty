from django import forms
from .models import Garden, Plant

class GardenForm(forms.ModelForm):
    class Meta:
        model=Garden
        fields='__all__'

class PlantForm(forms.ModelForm):
    class Meta:
        model=Plant
        fields={'plantname', 'plantdescr', 'isseed', 'dateplanted'}

#dateplanted = forms.DateField(widget = NumberInput(attrs={'type':'date'}))
#dateharvested = forms.DateField(widget = NumberInput(attrs={'type':'date'}))    