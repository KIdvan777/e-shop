from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404
from django.http import Http404

from app.models import App
from .models import Product
from carts.models import Cart

# # Create views here.

##### Class based View #############################################################################################################################################################

# List view

class ProductListView(ListView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        return context

    # custom query
    def get_queryset(self, *args, **kwargs):
        request =  self.request
        product_list = Product.objects.all()
        return product_list

# Detail view

class ProductDetailView(DetailView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        return context

    # custom query
    # def get_object(self, *args, **kwargs):
    #     request =  self.request
    #     pk = self.kwargs.get('pk')
    #     product_list = Product.objects.get_by_id(pk)
    #     if product_list is None:
    #         raise Http404("Product doesnt't exist!")
    #     return product_list

    def get_queryset(self, *args, **kwargs):
        request =  self.request
        pk = self.kwargs.get('pk')
        product_list = Product.objects.filter(pk=pk)
        return product_list

# Slug detail view

class ProductDetailSlugView(DetailView):
    object_list = App.objects.all()
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        context['cart'] = cart_obj
        # context['product_list'] = queryset
        return context

    # custom query
    def get_object(self, *args, **kwargs):
        request =  self.request
        slug = self.kwargs.get('slug')
        # product_list = get_object_or_404(Product, slug=slug)
        try:
            product_list = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            product_list = Product.objects.filter(slug=slug)
            return product_list.first()
        except:
            raise Http404("ebat")
        return product_list

    # def get_queryset(self, *args, **kwargs):
    #     request =  self.request
    #     pk = self.kwargs.get('slug')
    #     product_list = Product.objects.filter(slug=slug)
    #     return product_list

# Featured view

class ProductFeaturedListView(ListView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductFeaturedListView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        return context

    # custom query
    def get_queryset(self, *args, **kwargs):
        request =  self.request
        product_list = Product.objects.all().featured()
        return product_list

# Featured detail view

class ProductFeaturedDetailView(DetailView):
    # object_list = App.objects.all()
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductFeaturedDetailView, self).get_context_data(*args,**kwargs)
    #     print(context)
    #     object_list = App.objects.all()
    #     # queryset = Product.objects.all()
    #     context['object_list'] = object_list
    #     # context['product_list'] = queryset
    #     return context

    # custom query
    # def get_object(self, *args, **kwargs):
    #     request =  self.request
    #     pk = self.kwargs.get('pk')
    #     product_list = Product.objects.get_by_id(pk)
    #     if product_list is None:
    #         raise Http404("Product doesnt't exist!")
    #     return product_list

    # custom query
    # def get_queryset(self, *args, **kwargs):
    #     request =  self.request
    #     product_list = Product.objects.featured()
    #     return product_list



##### Function based View ###################################################################################################################################################################

# # shop view
#
# def shop_view(request):
#     object_list = App.objects.all()
#     product_list = Product.objects.all()
#     context={
#         'object_list':object_list,
#         'product_list':product_list
#     }
#     return render(request, "shop.html", context)


##### Function based View ###################################################################################################################################################################

# # detail view
#
# def detail_view(request, pk=None, *args, **kwargs):
#     object_list = App.objects.all()
#     product_list = Product.objects.all()
#
#     # instance = Product.objects.get(pk=pk)
#     # instance = get_object_or_404(Product, pk=pk)
#
# # Featured
#     # instance = Product.objects.get(pk=pk, featured=True)
#     # instance = get_object_or_404(Product, pk=pk, featured=True)
#
# # Exception for get() method ############################################################################################################33
#     # try:
#     #     instance = Product.objects.get(id=pk)
#     # except Product.DoesNotExist:
#     #     print('no product here')
#     #     raise Http404("Product doesnt't exist!")
#     # except:
#     #     print("hih")
#
# # Filter method ############################################################################################################################
#     # qs = Product.objects.filter(id=pk)
#     # if qs.exists() and qs.count() == 1:
#     #     instance = qs.first()
#     # else:
#     #     raise Http404("Product doesn't exist")
#
# # Custom object manager query ##################################################################################################
#     instance = Product.objects.get_by_id(pk)
#     if instance is None:
#         raise Http404("Product doesnt't exist!")
#
#     context={
#         'object_list':object_list,
#         'object':instance,
#         'product_list':product_list
#     }
#     return render(request, "product-detail.html", context)
