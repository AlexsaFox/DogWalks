from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse

from main.forms import DogCreateForm
from main.models import Dog, UserSettings, UserType


# Create your views here.

def index_page(request):
    context = {
        'dogs': Dog.get_all_dogs(),
    }
    return render(request, 'index.html', context)


def profile_page(request):
    user = request.user
    context = {
        'name': user.first_name,
        'surname': user.last_name,
        'dogs': user.usersettings.get_walked_dogs(),
        'id_card': user.userpass.id_card,
        'type': user.usersettings.get_type(),
    }
    return render(request, 'profile.html', context)


def dogs_list_page(request):
    context = {
        'dogs': Dog.get_all_dogs(),
    }
    return render(request, 'dogs_list.html', context)


def dogs_view_page(request, id):
    pass


def dogs_edit_page(request, id):
    pass


def dogs_create_page(request):
    form = DogCreateForm()
    if request.method == 'POST':
        if request.user.usersettings.type != UserType.CURATOR:
            raise Http404
        form = DogCreateForm(request.POST)
        if form.is_valid():
            dog = Dog(
                **form.cleaned_data,
                is_actual=True,
                curator=request.user,
            )
            dog.save()
            return redirect(reverse('dog_view', kwargs={'id':dog.id}))
    context = {
        'form': form,
    }
    return render(request, 'dog_create.html', context)
