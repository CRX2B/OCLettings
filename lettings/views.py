from django.shortcuts import render, get_object_or_404
from .models import Letting


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {
        'lettings_list': lettings_list,
    }
    return render(request, 'lettings/index.html', context)


def letting_detail(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
