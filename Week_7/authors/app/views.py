from django.shortcuts import render,redirect
from .models import author, publisher, book

# Create your views here.
def index(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        publisher_name = request.POST.get('publisher_name')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        website = request.POST.get('website')
        title = request.POST.get('title')
        publication_date = request.POST.get('date')
        author_instance = author.objects.create(first_name = first_name, last_name = last_name, email_address = email_address)
        publisher_instance = publisher.objects.create(publisher_name = publisher_name, street = street, city = city, state = state, country = country, website = website)
        book.objects.create(title = title, publication_date = publication_date, authors = first_name, publisher = publisher_instance)
        query_results = author.objects.all()
        context = { 'query_results' : query_results }
        return render(request, 'index.html', context)
    query_results = author.objects.all()
    context = { 'query_results' : query_results }
    return render(request, 'index.html', context)
