from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)

class Child(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    favorite_toy = models.CharField(max_length=100)

class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    ice_creams_available = models.ManyToManyField(IceCream)

class Parent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

class ChildOfParent(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
