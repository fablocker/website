from .models import Event
from .views import vote
from urlrouter.base import URLHandler


class RsvtRoutes(URLHandler):
    model = Event

    def show(self, request, event):
        return rsvp(request, event)

