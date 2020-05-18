
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/',views.login,name="login"),
    url(r'^register/',views.register,name="register"),
    url(r'^logout/',views.logout,name="logout")
    
]
