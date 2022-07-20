
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ccadmin/',views.ccadmin,name='ccadmin'),
]
