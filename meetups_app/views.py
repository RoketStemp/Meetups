from django.core.exceptions import ObjectDoesNotExist

from django.shortcuts import render, redirect

from .models import Meetup, Participants
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups_app/index.html', {
        'meetups': meetups
    })


def meetup_detail(request, slug):
    try:
        selected_meetup = Meetup.objects.get(slug=slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
            return render(request, 'meetups_app/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, was_created = Participants.objects.get_or_create(email=user_email)
                if was_created:
                    selected_meetup.participants.add(participant)
                    return redirect('confirm-registration', slug=slug)
                else:
                    try:
                        selected_meetup.participants.get(email=user_email)
                        registration_form.add_error('email', 'U\'ve already registered to this Meetup!')
                        return render(request, 'meetups_app/meetup-details.html', {
                            'meetup_found': True,
                            'meetup': selected_meetup,
                            'form': registration_form
                        })
                    except ObjectDoesNotExist:
                        selected_meetup.participants.add(participant)
                        return redirect('confirm-registration', slug=slug)

        return render(request, 'meetups_app/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except ObjectDoesNotExist:
        return render(request, 'meetups_app/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, slug):
    meetup = Meetup.objects.get(slug=slug)
    return render(request, 'meetups_app/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })
