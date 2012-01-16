from .models import Choice, Poll
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def vote(request, poll):
    error_message = None 
    if request.method == 'POST':
        try:
            selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # indicate the error
            error_message =  "You didn't select a choice."
        else:
            to_save = False
            if len(poll.voters) > 0:
                for cur_user in poll.voters:
                    if(request.user.id != cur_user):
                        to_save = True
                        break #found the one, stop looking
            else:
                to_save=True #no users have voted
                
            if to_save:
                poll.voters.append(request.user.id)
                poll.save()
                selected_choice.votes += 1
                selected_choice.save()
                #redirect them to keep from resubmitting the form
                return HttpResponseRedirect(poll.url)
            else:
                error_message = 'You have already voted in this poll!'
    return render(request, 'polls/poll_detail.html',
           {'poll': poll, 'error_message' : error_message}, context_instance=RequestContext(request))
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
'''         
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
    else:
        form = ContactForm()'''
          