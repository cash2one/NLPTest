# -*- coding: utf-8 -*-
from django.conf.urls import url
from tencent import views
from django.views.generic import TemplateView

urlpatterns = [ 
    #url(r'^market.html$', TemplateView.as_view(template_name="market/market.html")),
    

    #测试用
    url(r'test$',views.test, name='test'),

    #腾讯接口
    url(r'get_sentiment$',views.get_sentiment, name='get_sentiment'),
    url(r'get_keywords$',views.get_keywords, name='get_keywords'),
    url(r'get_synonym$',views.get_synonym, name='get_synonym'),
    url(r'get_classify$',views.get_classify, name='get_classify'),
    url(r'get_sensitivity$',views.get_sensitivity, name='get_sensitivity'),
    url(r'get_check$',views.get_check, name='get_check'),
    url(r'get_split$',views.get_split, name='get_split'),
]
