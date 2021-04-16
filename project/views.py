from django.shortcuts import render

def index(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html',{'title':'Dashboard'})