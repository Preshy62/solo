from django.urls import path
from .views import myapp 
from .views import contract
from .views import index
from .views import about
from .views import agroff
from .views import chem
from .views import dashboard
from .views import farm
from .views import farmerssignup
from .views import harv
from .views import prod
from .views import login
from .views import prof
from .views import signup
from .views import start
from .views import admin


urlpatterns = [
    path('', myapp, name='myapp'),
    path('index',index, name='index'),
    path('contract',contract, name='contract'),
    path('prod',prod, name='prod'),
    path('agroff',agroff, name='agroff'),
    path('chem',chem, name='chem'),
    path('chem',chem, name='prod'),
    path('about',about, name='about'),
    path('dashboard',dashboard, name='dashboard'),
    path('farm',farm, name='farm'),
    path('farmerssignup',farmerssignup, name='farmerssignup'),
    path('harv',harv, name='harv'),
    path('login',login, name='login'),
    path('prof',prof, name='prof'),
    path('signup',signup, name='signup'),
    path('start',start, name='start'),
    path('admin',admin, name='admin'),
   
]  
      
        # This will match /myapp/


