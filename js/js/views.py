import json
import time

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from data.adata import Adata


def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    print(id,pwd);
    return render(request, 'jq05.html');

def ajs01(request):
    now = time.time();
    return HttpResponse(time.ctime(now));

def ajs011(request):
    data = Adata().aj011();
    return HttpResponse(json.dumps(data),
                         content_type='application/json');

def ajs02(request):
    cmd = request.GET['cmd'];
    data = Adata().aj02(cmd);
    return HttpResponse(json.dumps(data),
                         content_type='application/json');

def ajs03(request):
    cmd = request.GET['cmd']
    data = Adata().aj03(cmd);
    return HttpResponse(json.dumps(data),
                        content_type='application/json');