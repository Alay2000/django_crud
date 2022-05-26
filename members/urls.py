from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('add/addrecord/',views.addrecord,name='addrecord'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit/editrecord/<int:id>',views.editrecord,name='editrecord')
]