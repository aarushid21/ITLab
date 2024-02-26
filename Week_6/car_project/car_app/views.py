from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Car

def index(request):
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model_name = request.POST.get('model_name')
        Car.objects.create(manufacturer=manufacturer, model_name=model_name)
        return redirect('car_detail', manufacturer=manufacturer, model_name=model_name)
    return render(request, 'car_app/index.html', {'manufacturers': ['Toyota', 'Honda', 'Ford']})

def car_detail(request, manufacturer, model_name):
    return render(request, 'car_app/car_detail.html', {'manufacturer': manufacturer, 'model_name': model_name})
