"""from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def index(request):
    return render(request, 'index.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form == 'Volvo':
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("https://www.volvocars.com/in/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html') """

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import student

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        subject = request.POST.get('subject')
        student.objects.create(name=name, roll_number=roll_number, subject=subject)
        return redirect('form_details', name=name, roll_number=roll_number, subject=subject)
    return render(request, 'index.html', {'subject': ['physics', 'chemistry', 'biology']})

def form_details(request, name, roll_number, subject):
    return render(request, 'form_details.html', {'name': name, 'roll_number': roll_number, 'subject':subject})

