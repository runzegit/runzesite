from django.conf.urls import url
from django.contrib import admin
from . import views
app_name='runze'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contato, name='contato'),
]
