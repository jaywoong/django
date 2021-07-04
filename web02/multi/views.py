from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def list(request):
    return render(request, 'list.html')
def chart(request):
    return render(request, 'chart.html')