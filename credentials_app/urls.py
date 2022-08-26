from . import views
from django.urls import path


urlpatterns = [
    path('register/',views.register,name='register.html'),
    path('login/',views.login,name='login.html'),
    path('index/',views.index,name='index.html'),
    
]
