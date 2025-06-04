from django.urls import path,include
from . import views


urlpatterns = [
    path('list/', views.list, name='list' ), 
    path('write/', views.write, name='write' ), 
    path('view/<int:bno>/', views.view, name='view' ), 
    
]
