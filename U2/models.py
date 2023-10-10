from django.db import models
from django.core.validators import MinValueValidator

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    occupation = models.CharField(max_length=100)

    def get_id_and_name(self):
        return f"{self.id} - {self.name}"

class Child(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    favorite_toy = models.CharField(max_length=100)

class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    quantity = models.PositiveIntegerField(validators=[MinValueValidator])

    def calculate_total_price(self):
        return self.price * self.quantity

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=200)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    ice_creams_available = models.ManyToManyField(IceCream)

    def save(self, *args, **kwargs):
        super(IceCreamKiosk, self).save(*args, **kwargs)
        self.location = f"{self.location} ({self.id})"

class Parent(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

class ChildOfParent(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()


for model in [Person, Child, IceCream, IceCreamKiosk, Parent, ChildOfParent]:
    for item in model.objects.all():
        if item.id % 2 != 0:
            item.delete()
