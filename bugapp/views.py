# coding:utf-8
from django.shortcuts import render,HttpResponse
from .forms import SenForm
from .tools import getTemplate_0,getTemplate_1,sen2NLPatt
from .NLPatt import NLPatt
from .NER import all_s

def index(request):
    sentence = ''

    if request.method == 'POST':
        form = SenForm(request.POST)
        print('POST')
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            print('提交数据合法')
        try:
            n = sen2NLPatt(sentence)
            print(n)
            template0 = getTemplate_0(n)
            template1= getTemplate_1(n)
        except Exception as e:
            print('生成模板失败')
            print(e)
            template0 = ['未能成功生成模板，请检查输入语句','未能成功生成模板，请检查输入语句']
            template1 = ['', '']
        return render(request,'home.html',{'template0':template0,'template1':template1,'form':form,'yuliao':all_s})
    return render(request,'home.html',{'yuliao':all_s})