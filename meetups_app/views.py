from django.shortcuts import render

from .models import Meetup


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups_app/index.html', {
        'meetups': meetups
    })
