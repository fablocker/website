from .forms import EventRsvpForm
from .models import Attendant
from django.shortcuts import render

def rsvp(request, event):
    if request.method == 'POST':
        form = EventRsvpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            attendant = Attendant()
            attendant.event = event
            attendant.email = email
            attendant.save()            
    else:
        form = EventRsvpForm()
    return render(request, 'rsvp/event_detail.html',
           {'form': form, 'event' : event,},)
        # Always return an HttpResponseRedirect after successfully dealing