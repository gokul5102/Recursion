from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='user-home'),
    path('covid-tracker/',views.cases,name='covid-tracker'),
    path('hospital-beds/',views.beds,name='hospital-beds'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')

]