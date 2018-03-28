from django.conf.urls import url
from . import views

urlpatterns = [
    # path('personal/', views.index, name='index'),
    url(r'^$', views.index, name='index')]
