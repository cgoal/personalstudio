# coding:utf-8

#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context={}
    context['title']='hell world'
    context['one']='title one'
    context['two']='title two'
    context['three']='title three'
    return render(request, 'index.html', context)