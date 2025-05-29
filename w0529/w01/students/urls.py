"""
URL configuration for w01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views

urlpatterns = [
    
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
    
    # html -> server 1.파라미터 2.api방식 3.js   <str:name>
    path('view/<int:no>/', views.view, name='view'),
    path('update/<int:no>/', views.update, name='update'),
    
]
