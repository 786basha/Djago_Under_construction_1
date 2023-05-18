from django.urls import path
from . import views

urlpatterns = [
    path('Home/',views.home1,name='home'),
    path('add',views.add,name='add'),
    path('edit',views.edit,name='edit'),
    path('update/<int:h>',views.update,name='update'),
    path('delete/<int:d>/',views.DELETE,name='del'),

    path('',views.DETAIL,name='detail'),
    path('Full - Details/',views.Fulldtl,name='fulldtl'),
    path('Details-Up/',views.Dtlup,name='updtl'),
    path('Dtl-Update/<int:id>',views.UpDtl,name='upup'),
    path('Details-Del',views.DelDtl,name='delDTL'),
    path('Dtl-Delete/<int:id>/',views.DELdtl,name='DELdtl'),
]