"""djangobarebone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core import view1, view2

urlpatterns = [
    path('admin/', admin.site.urls),

    # Unnecessary
    # path('accounts/', include('django.contrib.auth.urls')),  #

    # Login and Logout
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # View 1 and View 2
    path('view-1/', view1.view1, name="view1"),
    path('view-2/', view2.view2, name="view2"),

]
