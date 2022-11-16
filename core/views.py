from django.shortcuts import render

def Redmi(request):
    return render(request, 'qizil.html')

def Iphone(request):
    return render(request, 'qora.html')

def Samsung(request):
    return render(request, 'yashil.html')
# Create your views here.
