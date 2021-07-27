from django.contrib import admin

from .models import Meetup, Participants, Location


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_filter = ('location',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Participants)
admin.site.register(Location)
