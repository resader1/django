from django.urls import path,include
from . import views

app_name = 'comment'
urlpatterns = [
    path('list/', views.list, name='list'),
    
]