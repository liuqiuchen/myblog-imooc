from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    # 获取数据库里的一条记录
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index.html', {'article': article})
