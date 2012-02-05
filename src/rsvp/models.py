from django.db import models
from minicms.models import BaseContent

# Create your models here.
class Event(BaseContent):
    url = models.CharField('URL', max_length=200)
    show_share_buttons = models.BooleanField(default=False,
        help_text='Show buttons for sharing this event on Twitter, Facebook, etc.')

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url
    
class Attendant(models.Model):
    event = models.ForeignKey(Event)
    email = models.CharField(max_length=75)