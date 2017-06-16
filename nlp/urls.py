"""nlpeval URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView




urlpatterns = [
    url(r'^NLPPageTencent.html$', TemplateView.as_view(template_name="NLPPageTencent.html")),
    url(r'baiduGetView.html$', TemplateView.as_view(template_name="baidupage/baiduGetView.html"), name="baiduGetView"),
    url(r'baiduSimilar.html$', TemplateView.as_view(template_name="baidupage/baiduSimilar.html"), name="baiduSimilar"),
    url(r'tencentEmotion.html$', TemplateView.as_view(template_name="tencentpage/tencentEmotion.html"), name="tencentEmotion"),
    url(r'tencentClassify.html$', TemplateView.as_view(template_name="tencentpage/tencentClassify.html"), name="tencentClassify"),
    url(r'tencentKeyword.html$', TemplateView.as_view(template_name="tencentpage/tencentKeyword.html"), name="tencentKeyword"),
    url(r'tencentSimilarWord.html$', TemplateView.as_view(template_name="tencentpage/tencentSimilarWord.html"), name="tencentSimilarWord"),
    url(r'tencentCorrectWord.html$', TemplateView.as_view(template_name="tencentpage/tencentCorrectWord.html"), name="tencentCorrectWord"),
    url(r'bosonEmotion.html$', TemplateView.as_view(template_name="bosonpage/bosonEmotion.html"), name="bosonEmotion"),
    url(r'bosonAbstract.html$', TemplateView.as_view(template_name="bosonpage/bosonAbstract.html"), name="bosonAbstract"),
    url(r'bosonClassify.html$', TemplateView.as_view(template_name="bosonpage/bosonClassify.html"), name="bosonClassify"),
    url(r'bosonEntity.html$', TemplateView.as_view(template_name="bosonpage/bosonEntity.html"), name="bosonEntity"),
    url(r'bosonKeyword.html$', TemplateView.as_view(template_name="bosonpage/bosonKeyword.html"), name="bosonKeyword"),
    url(r'bosonSimilarword.html$', TemplateView.as_view(template_name="bosonpage/bosonSimilarword.html"), name="bosonSimilarword"),
    url(r'harbinEntity.html$', TemplateView.as_view(template_name="harbinpage/harbinEntity.html"), name="harbinEntity"),
    url(r'harbinRoleMark.html$', TemplateView.as_view(template_name="harbinpage/harbinRoleMark.html"), name="harbinRoleMark"),
    url(r'harbinDependency.html$', TemplateView.as_view(template_name="harbinpage/harbinDependency.html"), name="harbinDependency"),
    url(r'^index.html$', TemplateView.as_view(template_name="index.html")),
    url(r'^comparePage.html$', TemplateView.as_view(template_name="comparePage.html")),
    url(r'^NLPPageBaidu.html$', TemplateView.as_view(template_name="NLPPageBaidu.html")),
    url(r'^NLPPageBoson.html$', TemplateView.as_view(template_name="NLPPageBoson.html")),
    url(r'^NLPPageHarbin.html$', TemplateView.as_view(template_name="NLPPageHarbin.html")),
    url(r'^admin/', admin.site.urls),
    url(r'^baidu/', include('baidu.urls')),
    url(r'^tencent/', include('tencent.urls')),
    url(r'^boson/', include('boson.urls')),
    url(r'^harbin/', include('harbin.urls')),
    url(r'^baidupage/', include('baidu.urls')),
]
