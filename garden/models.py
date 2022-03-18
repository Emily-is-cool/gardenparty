from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE 

# Create your models here.

class GardenType(models.Model):
    typename=models.CharField('Name of Type:', max_length=250)
    typedescription=models.CharField('Description', max_length=300, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='gardentype'
        verbose_name_plural='gardentypes'

class Garden(models.Model):
    gardenname=models.CharField('Name your Garden:', max_length=250)
    gardentype=models.ForeignKey(GardenType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    gardendescription=models.TextField('Garden Description:', null=True, blank=True)
    datestarted=models.DateField

    def __str__(self):
        return self.gardenname

    class Meta:
        db_table='garden'
        verbose_name_plural='gardens'

class Plant(models.Model):
    plantname=models.CharField('Plant Name:', max_length=300)
    plantdescr=models.TextField('Plant Description:')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    isseed=models.BooleanField('Starting from seed?', default=False)
    dateplanted=models.DateField('Date Planted:')
    dateharvested=models.DateField(null=True, blank=True)
    gardenid=models.ForeignKey(Garden, on_delete=models.CASCADE)

    def __str__(self):
        return self.plantname

    class Meta:
        db_table='plant'
        verbose_name_plural='plants'