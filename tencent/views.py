# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from tencent_api import TencentNLP
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test(request):
	a = u'哈哈哈'
	return JsonResponse({'data': a, 'message': u'获取成功', 'status': 0})

#http://127.0.0.1:8000/tencent/get_sentiment
@csrf_exempt
def get_sentiment(request):
	text = request.POST.get('text', '')
	#text = '特斯拉很好，外观既漂亮又年轻,动力和操控性都不错'
	if text:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.testSentiment(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_keywords
@csrf_exempt
def get_keywords(request):
	title = request.POST.get('title', '')
	text = request.POST.get('text', '')
	if title and text:
		title = title.encode('utf-8')
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result=aip.testKeywords(title,text)
		except:
			result=aip.testKeywords(text,text)
		if result == -1:
			return JsonResponse({'data': u'未找到关键词', 'message': u'获取失败', 'status': 1})
		else:
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_synonym
@csrf_exempt
def get_synonym(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.lexicalSynonym(text)
			if result == -1:
				return JsonResponse({'data': u'未找到同义词', 'message': u'获取失败', 'status': 1})
			else:
				return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_classify
@csrf_exempt
def get_classify(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.textClassify(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_sensitivity
@csrf_exempt
def get_sensitivity(request):
	text = request.POST.get('text', '')
	ope = int(request.POST.get('type', ''))
	if text and ope:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.textSensitivity(text,ope)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_check
@csrf_exempt
def get_check(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.lexicalCheck(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/tencent/get_split
@csrf_exempt
def get_split(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = TencentNLP()
		try:
			result = aip.lexicalAnalysis(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

