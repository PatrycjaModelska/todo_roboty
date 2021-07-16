from django.shortcuts import render


def home_page(request):
    if request.method == 'POST':
        new_item = request.POST.get('item_text', '')
        return render(request, 'home.html', {'new_item_text': new_item,})
    return render(request, 'home.html')


