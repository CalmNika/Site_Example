from django.shortcuts import render

# Create your views here.
from .models import Person, IceCream

def some_view(request):
    person = Person.objects.get(id=1)
    id_and_name = person.get_id_and_name()

    ice_cream = IceCream.objects.get(id=1)
    total_price = ice_cream.calculate_total_price(quantity=3)