from django.shortcuts import render

# Create your views here.

from app.models import App
from .models import Cart


def cart_home(request):
    object_list = App.objects.all()

    # del request.session['cart_id']
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print('Cart ID exists')
        cart_obj = qs.first()
        if request.user.is_authenticated() and  cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id
    return render(request, "carts/home.html", {'object_list':object_list})
