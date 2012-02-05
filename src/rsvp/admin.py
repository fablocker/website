from django.contrib import admin
from minicms.admin import PageAdmin
from .models import Event, Attendant

class AttendantInline(admin.TabularInline):
	model = Attendant
	extra = 1

class EventAdmin(admin.ModelAdmin):
	inlines = [AttendantInline]
	fields = ('url', 'title', 'content', 'show_share_buttons')
	list_display = ('url', 'title', 'show_share_buttons')
	search_fields = ('url',)
	ordering = ('url',)

admin.site.register(Event, EventAdmin)
admin.site.register(Attendant)