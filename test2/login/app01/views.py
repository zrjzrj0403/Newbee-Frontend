from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from . import models
from django.core import serializers
import json
from django.forms import model_to_dict




def api_login(requst):
    name = requst.POST.get('name')
    # requst.session['name']=name
    pwd = requst.POST.get('pwd')
    result = models.User.objects.filter(name=name, pwd=pwd).first()
    if result:

        res = JsonResponse({'info': 'OK'})
        res.set_cookie('name', bytes(name, 'utf-8').decode('iso-8859-1'))
        # res.session['name'] =name
        # print(requst.COOKIES.get('name'))
        return res
    else:
        return JsonResponse({'info': 'Error'})


def api_get_cookie(requst):
    name = requst.COOKIES.get('name')
    if name:
        name = name.encode('iso-8859-1').decode('utf-8')
        return JsonResponse({'info': 'OK', 'name': name})
    else:
        return JsonResponse({'info': 'Error'})


def api_logout(requst):
    res = JsonResponse({'info': 'OK'})
    res.delete_cookie('name')
    return res


def api_get_information(requst):

    pagenumber=int(requst.GET.get('pagenumber'))
    pagesize=int(requst.GET.get('pagesize'))
    res={}
    data = models.User2.objects.values()[(pagenumber-1)*pagesize:pagesize*pagenumber]
    count=models.User2.objects.count()
    res['list'] = list(data)
    res['total'] = count
    res['info']='OK'
    return JsonResponse(res)


def api_deleteuser(requst):
    list=requst.GET.getlist('rows', [])
    res = JsonResponse({'info': 'OK'})
    for id in list:
        models.User2.objects.get(id=id).delete()
    return res

def api_search(requst):
    name=requst.GET.get('name')
    pagenumber = int(requst.GET.get('num'))
    pagesize = int(requst.GET.get('pagesize'))
    res = {}
    data = models.User2.objects.filter(user2_name=name)[(pagenumber-1)*pagesize:pagesize*pagenumber]
    count = models.User2.objects.filter(user2_name=name).count()
    res['total'] = count
    res['list'] = json.loads(serializers.serialize("json", data))
    res['list'] = dict(
    dataid = [d["fields"] for d in json.loads(serializers.serialize('json', data))])
    res['info'] = 'OK'
    return JsonResponse(res)
