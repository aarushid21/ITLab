from django.shortcuts import render,redirect
from .models import works, lives

# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        street = request.POST.get('street')
        city = request.POST.get('city')
        works_instance = works.objects.create(person_name = name, company_name = company, salary = salary)
        lives.objects.create(person_name = works_instance, street = street, city = city)
        query_results = works.objects.all()
        context = { 'query_results' : query_results }
        return render(request, 'index.html', context)
    query_results = works.objects.all()
    context = { 'query_results' : query_results }
    return render(request, 'index.html', context)

