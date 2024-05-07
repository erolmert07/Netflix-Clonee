from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',userLogin,name="login"),
    path('browse/',browse,name="browse"),
    path('createProfile/',createProfil,name="createProfil"),
    path('hesap/',hesap,name="hesap"),
    path('logout',userLogout,name="logout"),
    path('remove',removeAccount,name="remove")
]
