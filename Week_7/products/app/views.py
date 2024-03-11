from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import product

# Create your views here.
def index(request):
    if request.method =='POST':
        title = request.POST.get('name')
        price = request.POST.get('cost')
        description = request.POST.get('description')
        product.objects.create(title = title, price = price, description = description)
        query_results = product.objects.all()
        context = { 'query_results' : query_results }
        return render(request, 'index.html', context)
    query_results = product.objects.all()
    context = { 'query_results' : query_results }
    return render(request, 'index.html', context)
