from django.shortcuts import render

from main.models import Dog, UserSettings


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