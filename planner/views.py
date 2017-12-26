from django.http import HttpResponse
from django.views import generic
from planner.models import Calendar
from datetime import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the planner index.")


class CalendarListView(generic.ListView):
    template_name = 'planner/calendar_list.html'
    context_object_name = 'calendars'
    
    def get_queryset(self):
        return Calendar.objects.all()
    

class CalendarView(generic.DetailView):
    model = Calendar
    template_name = 'planner/calendar.html'
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CalendarView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['entries'] = self.get_object().get_entries(datetime.today(), 8)
        return context