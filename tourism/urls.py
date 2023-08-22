from django.urls import path
from . import views

urlpatterns={
    path('',views.home,name='home'),
    
    path('goa/',views.goa,name='goa'),
    path('lehladkah/',views.lehladkah,name='lehladkah'),
    path('kerela/',views.kerela,name='kerela'),
    path('andaman/',views.andaman,name='andaman'),
    path('dubai/',views.dubai,name='dubai'),
    path('singapore/',views.singapore,name='sinapore'),
    path('maldives/',views.maldives,name='maldives'),
    path('thailand/',views.thailand,name='thailand'),
    path('homeadd/',views.homeadd,name='homeadd'),
    path('addrecord/',views.addrecord,name='addrecord'),
    path('ttable/',views.ttable,name='ttable'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('homeupdate/<int:id>',views.homeupdate,name='homeupdate'),

}
