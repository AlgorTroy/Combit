"""PartTimeJobFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from MainApp.views import logout_page, register, home, login
# from django.contrib.auth.views import login
from django.contrib import admin
from MainApp import views


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', views.show_tile),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    # url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^accounts/login/$', login), # If user is not login it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^home/$', home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
]
