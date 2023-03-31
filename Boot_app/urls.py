from django.urls import path
from . import views

urlpatterns = [
    path('Admin_ID=123/',views.home,name='hm'),
    path('Register/',views.about,name='reg'),
    path('user-update/<int:h>/',views.usrup,name='usrup'),
    path('user-delete/<int:u>/',views.usrdel,name='usrdel'),
]