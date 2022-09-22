from django.urls import path,include
from . import views

urlpatterns =[
    path("leads/",views.get_mail,name="leads"),
    path("",views.index,name=""),
]