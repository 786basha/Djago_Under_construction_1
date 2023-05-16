from django.urls import path
from . import views

urlpatterns = [
    path('Home/',views.home1,name='home'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<int:h>',views.update,name='update'),
    path('delete/<int:d>/',views.DELETE,name='del'),
]