from django.shortcuts import render, redirect
from .models import student

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        student.objects.create(username=username, password=password, contact_number=contact_number, email=email)
        return redirect('form_details', username=username, password=password, contact_number=contact_number, email=email)
    return render(request, 'index.html')

def form_details(request, username, password, contact_number, email):
    return render(request, 'form_details.html', {'username': username, 'contact_number': contact_number, 'email':email, 'password':password})

