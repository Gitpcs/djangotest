from django.http import HttpResponse
from django.shortcuts import render   #渲染

def hello(request):
    return HttpResponse("配置视图")
    # 给视图   下一步配置视图
    # content={}
    # content['list']="环球华信"
    # list="环球华信"
    # return render(request,'hello.html',content)