"""company URL Configuration

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
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from house import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url('add-asset/',views.AssetList.as_view()),
    url('assets/all/',views.AssetList.as_view()),
    url('add-work/',views.WorkList.as_view()),
    url('add-worker/',views.WorkerList.as_view()),
    url('allocate-task/',views.AllocateworkList.as_view()),
    url('get-tasks-for-worker/',views.AllocateworkList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



