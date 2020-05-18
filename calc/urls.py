from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name="home"),
    url(r'^add1',views.add1,name="add"),
]