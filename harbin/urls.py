# -*- coding: utf-8 -*-
from django.conf.urls import url
from harbin import views
from django.views.generic import TemplateView

urlpatterns = [ 
    #url(r'^market.html$', TemplateView.as_view(template_name="market/market.html")),
    

    #测试用
    url(r'test$',views.test, name='test'),

    #harbin接口
    url(r'get_split$',views.get_split, name='get_split'),
    url(r'get_lexical$',views.get_lexical, name='get_lexical'),
    url(r'get_dependency$',views.get_dependency, name='get_dependency'),
    url(r'get_mark$',views.get_mark, name='get_mark'),
]
