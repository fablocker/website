from .models import Poll
from .views import vote
from urlrouter.base import URLHandler


class PollRoutes(URLHandler):
    model = Poll

    def show(self, request, poll):
        return vote(request, poll)

