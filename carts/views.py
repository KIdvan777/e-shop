from django.shortcuts import render

# Create your views here.

from app.models import App

def cart_home(request):
    object_list = App.objects.all()
    return render(request, "carts/home.html", {'object_list':object_list})
