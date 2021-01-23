from django.shortcuts import render
from .models import products
from .models import people

# Create your views here.
def home(request):
    context = {}
    return render(request, 'dynamicwebsite/home.html', context)

def productslist(request):
    context = {}
    context['products'] = products.objects.all()
    return render(request, 'dynamicwebsite/products.html', context)  

def peoplelist(request):
    context ={}
    context['people'] = people.objects.all()
    return render(request,'dynamicwebsite/people.html',context)

def contactus(request):
    context = {}
    return render(request, 'dynamicwebsite/contactus.html',context)  

