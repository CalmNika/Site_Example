from django.shortcuts import render

# Create your views here.
from .models import Person, IceCream

def some_view(request):
    person = Person.objects.get(id=1)
    id_and_name = person.get_id_and_name()

    ice_cream = IceCream.objects.get(id=1)
    total_price = ice_cream.calculate_total_price(quantity=3)

from U2.models import Person
person_data = Person.objects.values('name', 'age')

from U2.models import Person, Child, IceCream, IceCreamKiosk, Parent, ChildOfParent

for model in [Person, Child, IceCream, IceCreamKiosk, Parent, ChildOfParent]:
    model.objects.exclude(id__mod=2).delete()