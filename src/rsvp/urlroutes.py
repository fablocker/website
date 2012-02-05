from .models import Event
from .views import rsvp
from urlrouter.base import URLHandler


class RsvpRoutes(URLHandler):
    model = Event

    def show(self, request, event):
        return rsvp(request, event)

