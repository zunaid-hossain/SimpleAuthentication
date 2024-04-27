from django.urls import path
from . import views


urlpatterns = [    
    path('signup',views.register,name='signup'),
    path('login',views.login_user,name='login'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout_user,name='logout'),
    path('Change_pass',views.Change_pass,name='Pass'),
    path('Fpass',views.fChange_pass,name='fpass'),

]
