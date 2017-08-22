from django.conf.urls import url
from django.contrib import admin
from . import views
app_name='producao'

urlpatterns = [
	url(r'^$', views.home, name='home'),
]
