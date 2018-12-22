from django.shortcuts import render

# Create your views here.

from app.models import App
from .models import Cart


def cart_home(request):
    object_list = App.objects.all()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()

    return render(request, "carts/home.html", {'object_list':object_list})
