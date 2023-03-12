from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='ab'),
    path('user-update/<int:h>/',views.usrup,name='usrup'),
    path('user-delete/<int:u>/',views.usrdel,name='usrdel'),
]