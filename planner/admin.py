from django.contrib import admin

from planner.models import Calendar, CalendarEntry


class CalendarEntryInline(admin.TabularInline):
    model = CalendarEntry
    extra = 1
    
class CalendarAdmin(admin.ModelAdmin):
    inlines = [CalendarEntryInline]

admin.site.register(Calendar, CalendarAdmin)
