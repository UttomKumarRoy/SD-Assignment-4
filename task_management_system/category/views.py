from django.shortcuts import render, redirect
from .models import TaskCategory
from .forms import CategoryForm

def add_category(request):
    form = CategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add_category')

    return render(request, 'category/add_category.html', {'form': form})
