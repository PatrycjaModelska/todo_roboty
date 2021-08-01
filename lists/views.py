from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import Item, List
from .forms import ItemForm


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        item = Item.objects.create(text=request.POST['text'], list=list_)
        try:
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "Element nie może być pusty"
            item.delete()

    return render(request, 'list.html', {'list': list_, 'error': error, 'form': ItemForm()})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        error = "Element nie może być pusty"
        list_.delete()
        return render(request, 'home.html', {'form': ItemForm(), 'error': error})
    return redirect(list_)
