from django.urls import re_path
from user import views


urlpatterns = [
    re_path(r'^farmer$', views.FarmerList.as_view()),
    re_path(r'^farmer/(?P<pk>[0-9]+)$', views.FarmerDetail.as_view()),
    re_path(r'^customer$', views.CustomerList.as_view()),
    re_path(r'^customer/(?P<pk>[0-9]+)$', views.CustomerDetail.as_view()),
    re_path(r'^address$', views.AddressList.as_view()),
    re_path(r'^address/(?P<pk>[0-9]+)$', views.AddressDetail.as_view()),
    re_path(r'^customer/(?P<customer_pk>[0-9]+)/address$', views.AddressForCustomer.as_view()),
    re_path(r'^login$', views.Login.as_view()),
    re_path(r'^farmer/email_verify/(?P<token>.*)', views.FarmerEmailVerifyView.as_view()),
    re_path(r'^customer/email_verify/(?P<token>.*)', views.CustomerEmailVerifyView.as_view()),
    re_path(r'^admin/email_verify/(?P<token>.*)', views.AdminEmailVerifyView.as_view()),
    re_path(r'^admin/(?P<pk>[0-9]+)$', views.AdminDetail.as_view()),
    re_path(r'^admin$', views.AdminList.as_view()),
    re_path(r'^register$', views.Register.as_view()),
]

