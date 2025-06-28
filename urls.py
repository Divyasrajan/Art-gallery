from django.urls import path
from .views import *
urlpatterns = [
   
    path('',addhome, name='home'),
    path('addhome/',addhome, name='home'),
    path('addabout/',addabout, name='about'),
    path('addcategories/',addcategories, name='categories'),
    path('adddownload/',adddownload, name='download'),
    path('loginpage/',loginpage, name='login'),
    path('addlogout/',addlogout, name='logout')

]