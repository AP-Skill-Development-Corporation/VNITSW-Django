"""ExampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from DemoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gh/',views.greet),
    path('ghr/',views.demo),
    path('w/<str:y>/',views.b),
    path('k/<str:a>/<int:r>/',views.st),
    path('mg/<str:en>/<int:sa>/<str:dg>/',views.em),
    path('v/<str:cmp>/<str:ename>/',views.cpp),
    path('n/<str:d>/',views.fy),
    path('mk/',views.dd),
    path('p/',views.hk),
    path('b/<str:c>/',views.fbn),
    path('z/<str:rn>/<str:sn>/<str:sb>/<int:sy>/<str:cg>/',views.std),
    path('bz/',views.fm),
    path('y/',views.btp),
    path('d/',views.eda,name="emm"),
    path('ep/<int:g>/',views.emup,name="epd"),
    path('ed/<int:q>/',views.edl,name="edd"),
    path('',views.edd,name="el"),
    path('epp/<int:c>/',views.empp,name="epdt"),
]
