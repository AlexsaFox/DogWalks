from django.shortcuts import render

from main.models import Dog


# Create your views here.

def index_page(request):
    context = {
        'dogs': Dog.get_all_dogs(),
    }
    return render(request, 'index.html', context)

