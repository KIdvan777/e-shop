from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url
from django import forms


from app.models import App, Slider
from products.models import Product
from carts.models import Cart

# Create your views here.



User = get_user_model()

##### Login #################################################################################################################################################

class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                         "placeholder":"Name"
                                                        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                         "placeholder":"Password"
                                                        }))

##### Register ##################################################################################################################################

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                         "placeholder":"Name"
                                                        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
                                                         "placeholder":"Email"
                                                        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",
                                                         "placeholder":"Password"
                                                        }))


    def clean_username(self):
        User = get_user_model()
        username = self.cleaned_data('name')
        qs = User.objects.filter(username=username)
        if qs.exist():
           raise forms.ValidationError("Username is taken")
        return  username

#  login view #####################################################################################################################################################

def login_view(request):
    object_list = App.objects.all()
    login_form = LoginForm(request.POST or None)
    reg_form = RegisterForm(request.POST or None)

    context={
        'object_list':object_list,
        'login_form':login_form,
        'reg_form':reg_form
    }

    next_ =  request.GET.get('next')
    next_post =  request.POST.get('next')
    redirect_path = next_ or next_post or None
    if login_form.is_valid():
        username = login_form.cleaned_data.get("name")
        password = login_form.cleaned_data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
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
