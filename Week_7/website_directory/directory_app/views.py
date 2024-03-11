from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, PageForm
from .models import Category, Page

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'directory_app/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            # Update the number of sites for the associated category
            category = page.category
            category.num_sites += 1
            category.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'directory_app/add_page.html', {'form': form})

def page_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    print("Page accessed:", page)  # Check if the page is being accessed
    page.views += 1
    page.save()
    print("Page views updated:", page.views)  # Check if the views count is updated
    return render(request, 'directory_app/page_detail.html', {'page': page})


def index(request):
    categories = Category.objects.all()
    return render(request, 'directory_app/index.html', {'categories': categories})
