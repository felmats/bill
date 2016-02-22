"""bill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^company/$', views.company_list, name="company_list"),
    url(r'^company/add/$', views.company_edit, name="company_add"),
    url(r'^company/edit/(?P<company_cd>\d+)/$', views.company_edit, name="company_edit"),
    url(r'^company/del/(?P<company_cd>\d+)/$', views.company_del, name="company_del"),
]
