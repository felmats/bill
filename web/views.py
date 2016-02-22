from django.shortcuts import render
from django.http import HttpResponse

from web.models import Company

def company_list(request):
    """一覧"""
    #return HttpResponse("一覧")
    #companies = Company.objects.all().order_by('company_cd')
    return render(request,
                  'web/company_list.html',
                  )


def company_edit(request, company_cd=None):
    """編集"""
    return HttpResponse('編集')


def company_del(request, company_cd):
    """削除"""
    return HttpResponse('削除')
