from django import forms
from django.contrib.auth import get_user_model


##### Contact ###########################################################################################################################

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                         "placeholder":"Name"
                                                        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control",
                                                         "placeholder":"Email"
                                                        }))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",
                                                         "placeholder":"Subject"
                                                        }))
    message = forms.CharField(widget=forms.Textarea(attrs={"id":"message",
                                                         "class":"form-control",
                                                         "placeholder":" Your message here"
                                                        }))

    def clean_email(self):
        email = self.cleaned_data.get("name")
        if not "@" in email:
            raise forms.ValidationError("Email has to be g@")
        return email

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
