from django.db import models
from djangotoolbox import fields
from datetime import datetime
from minicms.models import BaseContent
from django.contrib.auth.models import User

class Poll(models.Model):
    url = models.CharField('URL', max_length=256)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    voters = fields.ListField(models.ForeignKey(User), editable=False)
    
    def __unicode__(self):
        return self.question
		
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
	was_published_today.short_description = 'Published today?'
    
    #this is required for URLRouter
    def get_absolute_url(self):
        return self.url

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice