import random
import os

from django.db import models

##### Path to image ##################################################################################################################################

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

# Create your models here.

###### Models ############################################################################################################################################################

class Social(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    icon = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=255)
    slug =  models.CharField(max_length=255)
    url =  models.CharField(max_length=255)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    social_links = models.ManyToManyField(Social)
    pages = models.ForeignKey(Page)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=255)
    span = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_2 = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.name
