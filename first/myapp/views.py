from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # トップページ
    context = {
        'name':'miya',
    }
    return render(request,'myapp/index.html',context)

def about(request):
    return render(request,'myapp/about.html')

def info(request):
    return render(request,'myapp/info.html')