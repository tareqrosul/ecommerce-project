
from django.contrib import admin
from django.urls import path
from . import views
#from django.conf.urls import url,include
from django.urls import include, path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user_end.urls')),
    # path('',views.homepage,name='home'),
    # path('eggs/',views.eggs),
    path('count/',views.count,name='tareq'),
    path('new/',views.new),
    # path('product/',views.prod,name='rosul'),
     path('',include('user_end.urls')),
    #path('index/',views.index,name='ind'),

]

urlpatterns+= staticfiles_urlpatterns()



































"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
