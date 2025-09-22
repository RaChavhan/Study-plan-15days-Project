from django.urls import path, include
from .views import RegisterAPI, ProfileAPI


urlpatterns = [
    # path("index/",views.index,name='index'),
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('profile/', ProfileAPI.as_view(), name='profile'),

]
