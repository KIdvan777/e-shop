from django.shortcuts import render

# Create your views here.

def cart_home(request):

    # key = request.session.session_key
    # print(key)
    request.session['first_name'] = "hask777"
    return render(request, "carts/home.html", {})
