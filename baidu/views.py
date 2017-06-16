# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from baidu_api import BaiduNLP
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
	a = u'哈哈哈'
	return JsonResponse({'data': a, 'message': u'获取成功', 'status': 0})

#http://127.0.0.1:8000/baidu/get_comment
@csrf_exempt
def get_comment(request):
	text = request.POST.get('text', '')
	ope = request.POST.get('type', '')
	#text = '特斯拉很好，外观既漂亮又年轻,动力和操控性都不错'
	if text and ope:
		text = text.encode('utf-8')
		options = {}
		options['type'] = int(ope)
		aip = BaiduNLP()
		try:
			result = aip.commenttag(text,options)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/baidu/get_similarity
@csrf_exempt
def get_similarity(request):
	text1 = request.POST.get('text1', '')
	text2 = request.POST.get('text2', '')
	# text1 = '焦鹏很帅,焦鹏牛逼,焦鹏是我大哥'
	# text2 = '特斯拉很好，外观既漂亮又年轻,动力和操控性都不错'
	if text1 and text2:
		text1 = text1.encode('utf-8')
		text2 = text2.encode('utf-8')
		aip = BaiduNLP()
		result=aip.simnet(text1,text2)
		return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/baidu/get_split
@csrf_exempt
def get_split(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = BaiduNLP()
		try:
			result=aip.wordseg(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

