import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myanalysis import Myanalysis


def home(request):
    return render(request, 'index.html');

def d1(request):
    context = {'section':'d1.html'};
    return render(request, 'index.html',context);
def d1s(request):
    option = request.GET['option'];
    print(option);
    data = Myanalysis.Titanic().d1s(option);
    return HttpResponse(json.dumps(data), content_type='application/json');

def d2(request):
    context = {'section':'d2.html'};
    return render(request, 'index.html',context);
def d3(request):
    context = {'section':'d3.html'};
    return render(request, 'index.html',context);
def d4(request):
    context = {'section':'d4.html'};
    return render(request, 'index.html',context);
def d5(request):
    context = {'section':'d5.html'};
    return render(request, 'index.html',context);
def geo(request):
    context = {'section':'geo.html'};
    return render(request, 'index.html',context);
