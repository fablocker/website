from .forms import EventRsvpForm
from .models import Attendant
from django.shortcuts import render

def rsvp(request, event):
    error = None
    saved = False
    if request.method == 'POST':
        form = EventRsvpForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            if(Attendant.objects.filter(email = form_email, event = event).exists()):
                    error = "Thanks! This e-mail has already been registered : ) " \
                        "You can register another though..."
            else:
                    attendant = Attendant()
                    attendant.event = event
                    attendant.email = form_email
                    attendant.save()
                    saved = True
    else:
        data = {}
        if request.user.is_authenticated():
            usermail = request.user.email
            if(usermail):
                data = { "email" : usermail }
                form = EventRsvpForm(data)
        else:
            form = EventRsvpForm()
    return render(request, 'rsvp/event_detail.html',
           {'form': form, 'event' : event, 'error': error, 'saved': saved},)
