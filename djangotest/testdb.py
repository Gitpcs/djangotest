from django.http import HttpResponse
from django.shortcuts import render
from add.models import addStu

def add(request):
    stu1=addStu(name='张三',sex='男',age='20')
    stu1.save()
    return render(request,'tjxs.html')

def select(request):
    list=addStu.objects.filter(id=1)
    return render(request,'list.html',{'list':list})

def update(request):
    x1=addStu.objects.get(id=1)
    x1.age='80'
    x1.save()
    list=addStu.objects.all()
    return render(request,'update.html',{'list':list})

def delete(request):
    y1=addStu.objects.get(id=3)
    y1.delete()
    list=addStu.objects.all()
    return render(request,'sc.html',{'list':list})