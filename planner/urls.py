from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'planner'

urlpatterns = [
    path('', views.CalendarListView.as_view(), name='index'),
    
    # TODO: Convert to path
    url(r'^(?P<pk>[0-9]+)/$', views.CalendarView.as_view(), name='calendar')
]