from django.shortcuts import render
from .models import products

# Create your views here.
def home(request):
    context = {}
    return render(request, 'dynamicwebsite/home.html', context)

def products(request):
    context = {}
    context['products'] = products.objects.all()
    return render(request, 'dynamicwebsite/products.html', context)  

def people(request):
    context ={}
    context['people'] = people.objects.all()
    return render(request,'dynamicwebsite/people.html',context)

def contactus(request):
    context = {}
    return render(request, 'dynamicwebsite/contactus.html',context)  

