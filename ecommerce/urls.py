from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin

from .views import (home_view, login_view, shop_view, detail_view, cart_view, blog_view, checkout_view,
blog_single_view, contact_view, page_404_view)

from carts.views import cart_home

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^shop-fbv/$', shop_view, name='shop'),
    url(r'^product-fbv/(?P<pk>\d+)/$', detail_view, name='product'),
    # url(r'^cart/$', cart_view, name='cart'),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^login/$', login_view, name='login'),
    url(r'^contact/$', contact_view, name='contact'),
    url(r'^blog/$', blog_view, name='blog'),
    url(r'^blog-single/$', blog_single_view, name='blog-single'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^404/$', page_404_view, name='404'),

    
    url(r'^products/', include("products.urls", namespace='products')),
    url(r'^search/', include("search.urls", namespace='search')),
    # url(r'^shop/$', ProductListView.as_view()),
    # url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^product/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
