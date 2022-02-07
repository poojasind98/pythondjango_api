# from django.urls import path
from django.conf.urls import url
from first_api_app import views

urlpatterns=[
    url(r'^$',views.index, name='index'),
]
