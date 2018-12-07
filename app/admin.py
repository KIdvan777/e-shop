from django.contrib import admin

# Register your models here.

from .models import App, Slider, Social, Page

admin.site.register(App)

admin.site.register(Slider)

admin.site.register(Social)

admin.site.register(Page)
