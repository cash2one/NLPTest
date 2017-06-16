# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import url, include
from baidu import views
from django.views.generic import TemplateView

urlpatterns = [ 

    

    #测试用
    url(r'test$',views.test, name='test'),

    #百度接口
    url(r'get_comment$',views.get_comment, name='get_comment'),
    url(r'get_similarity$',views.get_similarity, name='get_similarity'),
    url(r'get_split$',views.get_split, name='get_split'),
]
