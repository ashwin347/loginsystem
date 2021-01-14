from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.validate,name='validate'),
    path('signup',views.signup,name='signup'),
]