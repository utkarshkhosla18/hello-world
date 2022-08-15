from django.urls import re_path
from order import views
from order import paypalviews
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^customer/(?P<customer_pk>[0-9]+)/order$', views.CustomerOrderView.as_view()),
    re_path(r'^farmer/(?P<farmer_pk>[0-9]+)/order$', views.FarmerOrderView.as_view()),
    re_path(r'^farmer/order$', views.ALLFarmerOrderView.as_view()),
    re_path(r'^customer/order$', views.ALLCustomerOrderView.as_view()),
    re_path(r'^customer/paypal$', paypalviews.PaypalImpl.as_view()),
    re_path(r'^paypal/pay$', paypalviews.PaypalImpl.as_view())
    # re_path(r'^farmer/(?P<farmer_pk>[0-9]+)/order$', views.FarmerOrderView.as_view()),
    # re_path(r'^category/(?P<pk>[0-9]+)$', views.CategoryDetail.as_view()),
    # re_path(r'^product$', views.ProductList.as_view()),
    # re_path(r'^product/(?P<pk>[0-9]+)$', views.ProductDetail.as_view()),
    # re_path(r'^product/(?P<keyword>[a-zA-Z].*)$', views.ProductSearch.as_view()),
    # re_path(r'^farmer/(?P<farmer_pk>[0-9]+)/product$', views.ProductForFarmer.as_view()),
    # re_path(r'^category/(?P<category_pk>[0-9]+)/product$', views.ProductForCategory.as_view()),
    # # re_path(r'^customer/(?P<customer_pk>[0-9]+)/cart$', views.CartForCustomer.as_view()),
    # re_path(r'^customer/(?P<customer_pk>[0-9]+)/cart$', views.CartForCustomer.as_view()),
    # re_path(r'^order$', views.OrderView.as_view()),
]
