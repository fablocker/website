from .models import Choice, Poll
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def vote(request, poll):
    error_message = None 
    already_voted = True #assume the worst
    cur_voter = request.user.email
    if len(poll.voters) > 0:
		for past_voter in poll.voters:
			if(cur_voter == past_voter):
				already_voted = True
				break #found the one, stop looking
			else:
				already_voted = False #if this never gets reset
    else:
		already_voted=False #no users have voted
    if request.method == 'POST':
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # indicate the error
            error_message =  "You didn't select a choice."
        else:
            if not already_voted:
                poll.voters.append(cur_voter)
                poll.save()
                selected_choice.votes += 1
                selected_choice.save()
                #redirect them to keep from resubmitting the form
                return HttpResponseRedirect(poll.url)
            else:
                error_message = 'You have already voted in this poll!'
    return render(request, 'polls/poll_detail.html',
           {'poll': poll, 'error_message' : error_message, 'already_voted': already_voted}, context_instance=RequestContext(request))
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
