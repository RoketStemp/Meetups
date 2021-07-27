from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from .models import Meetup


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups_app/index.html', {
        'meetups': meetups
    })


def meetup_detail(request, slug):
    try:
        meetup = Meetup.objects.get(slug=slug)
        return render(request, 'meetups_app/meetup-details.html', {
            'meetup': meetup,
            'meetup_found': True
        })
    except ObjectDoesNotExist:
        return render(request, 'meetups_app/meetup-details.html', {
            'meetup_found': False
        })
