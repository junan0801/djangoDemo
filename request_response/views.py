import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse


# Create your views here.


def weather(request, city, year):
    print(year, city)
    return HttpResponse('Beijing')


def get_query_params(request):
    query_dict = request.GET
    listg = query_dict.get('a')
    return HttpResponse('get_query_params')


# POST方法获取表单数据
def get_form_data(request):
    query_dict = request.POST
    print(query_dict.getlist('like'))
    return HttpResponse('get_form_data')


def get_json(request):
    json_bytes = request.body
    json_str = json_bytes.decode()
    dictname = json.loads(json_str)
    print(dictname)
    return HttpResponse('get_json')


def get_user(request):
    print(request.user)
    return HttpResponse('GET_JSON')


def response_demo(request):
    return HttpResponse(content='Hello', content_type='text/plain', status=201)
