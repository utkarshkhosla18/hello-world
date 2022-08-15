from django.urls import re_path
from product import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    re_path(r'^category$', views.CategoryList.as_view()),
    re_path(r'^category/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),
    re_path(r'^product$', views.ProductList.as_view()),
    re_path(r'^product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view()),
    re_path(r'^farmer/(?P<farmer_pk>[0-9]+)/product$', views.ProductForFarmer.as_view()),
    re_path(r'^category/(?P<category_pk>[0-9]+)/product$', views.ProductForCategory.as_view()),
    # re_path(r'^customer/(?P<customer_pk>[0-9]+)/cart$', views.CartForCustomer.as_view()),
    re_path(r'^customer/(?P<customer_pk>[0-9]+)/cart$', views.CartForCustomer.as_view()),
    re_path(r'^product/(?P<keyword>[a-zA-Z].*)$', views.ProductSearch.as_view()),
    re_path(r'^customer/(?P<customer_pk>[0-9]+)/cart/(?P<cart_pk>[0-9]+)', views.CartView.as_view())
]

# Adding this lets you use filename extensions on URLs to provide an endpoint for a given media type.
# For example you can get endpoint data in json representation or html static file
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])