from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.shortcuts import render

# Create your views here.

from app.models import App, Slider
from products.models import Product
from .forms import ContactForm, LoginForm, RegisterForm


# home view
def home_view(request):
    print(request.session.get("first_name",  'Unknown'))
    object_list = App.objects.all()
    product_list = Product.objects.all()
    slider_list = Slider.objects.all()
    context={
        'object_list':object_list,
        'slider_list':slider_list,
        'product_list':product_list
    }
    return render(request, "index.html", context)

# shop view

def shop_view(request):
    object_list = App.objects.all()
    product_list = Product.objects.all()
    context={
        'object_list':object_list,
        'product_list':product_list
    }
    return render(request, "shop.html", context)

# detail view

def detail_view(request, pk=None, *args, **kwargs):
    object_list = App.objects.all()
    product_list = Product.objects.all()

    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

# Featured
    # instance = Product.objects.get(pk=pk, featured=True)
    # instance = get_object_or_404(Product, pk=pk, featured=True)

# Exception for get() method ############################################################################################################33
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesnt't exist!")
    # except:
    #     print("hih")

# Filter method ############################################################################################################################
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

# Custom object manager query ##################################################################################################
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesnt't exist!")

    context={
        'object_list':object_list,
        'object':instance,
        'product_list':product_list
    }
    return render(request, "product-detail.html", context)


#  login view

User = get_user_model()

def login_view(request):
    object_list = App.objects.all()
    login_form = LoginForm(request.POST or None)
    reg_form = RegisterForm(request.POST or None)

    context={
        'object_list':object_list,
        'login_form':login_form,
        'reg_form':reg_form
    }
    # print("User logged in")
    # print(request.user.is_authenticated())

    if login_form.is_valid():
        # print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("name")
        password = login_form.cleaned_data.get("password")
        # print(username)
        # print(password)
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # context['login_form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")

    if reg_form.is_valid():
        print(reg_form.cleaned_data)
        username = reg_form.cleaned_data.get("name")
        email = reg_form.cleaned_data.get("email")
        password = reg_form.cleaned_data.get("password")
        print(username)
        print(email)
        print(password)
        new_user = User.objects.create_user(username, email, password)
        print(new_user)

    return render(request, "login.html", context)


#  contact view ###############################################################################################################################

def contact_view(request):
    contact_form = ContactForm(request.POST or None)
    object_list = App.objects.all()
    context={
        'object_list':object_list,
        'form':contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "test.html", context)


#  checkout view ###############################################################################################################################################

def checkout_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "checkout.html", context)

#  cart view
def cart_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "cart.html", context)

#  blog view
def blog_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "blog.html", context)


#  blog-single  view
def blog_single_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "blog-single.html", context)

#  404  view
def page_404_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "404.html", context)
