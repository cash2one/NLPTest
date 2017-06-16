# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from ltpcloud import Ltpnlp
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def test(request):
	a = u'哈哈哈'
	return JsonResponse({'data': a, 'message': u'获取成功', 'status': 0})

#http://127.0.0.1:8000/harbin/get_split
@csrf_exempt
def get_split(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = Ltpnlp()
		try:
			result=aip.fenci(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/harbin/get_lexical
@csrf_exempt
def get_lexical(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = Ltpnlp()
		try:
			result = aip.lexicalAnalysis(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/harbin/get_dependency
@csrf_exempt
def get_dependency(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = Ltpnlp()
		try:
			result = aip.textDependency(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

#http://127.0.0.1:8000/harbin/get_mark
@csrf_exempt
def get_mark(request):
	text = request.POST.get('text', '')
	if text:
		text = text.encode('utf-8')
		aip = Ltpnlp()
		try:
			result = aip.wordmark(text)
			return JsonResponse({'data': result, 'message': u'获取成功', 'status': 0})
		except:
			return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})
	else:
		return JsonResponse({'data': '', 'message': u'获取失败', 'status': 1})

