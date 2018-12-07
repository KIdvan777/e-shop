from django.shortcuts import render
from django.views.generic import ListView
from app.models import App
from products.models import Product

# Create your views here.

# List view

class SearchProductView(ListView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        context['query'] = self.request.GET.get('q')
        return context

    # custom query
    def get_queryset(self, *args, **kwargs):
        request =  self.request
        print(request.GET)
        method_dict = request.GET
        query = method_dict.get('q',None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
