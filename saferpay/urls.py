from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^notify/(?P<notify_token>.+)/$', views.NotifyView.as_view(), name='saferpay-notify'),
]
