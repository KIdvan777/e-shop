from django.shortcuts import render

# Create your views here.

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None: #and isinctance(cart_id, int):
        print('create new cart')
        request.session['cart_id'] = 12
    else:
        print('Cart exists')

    request.session['user'] = request.user.username
    return render(request, "carts/home.html", {})
