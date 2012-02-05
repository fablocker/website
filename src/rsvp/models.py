from django.db import models
from minicms.models import Page

# Create your models here.
class Event(Page):
    #this is required for URLRouter
    def get_absolute_url(self):
        return self.url
    
class Attendant(models.Model):
    event = models.ForeignKey(Event)
    email = models.CharField(max_length=75)