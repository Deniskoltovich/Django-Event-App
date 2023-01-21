import datetime as dt

from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Event


def create_event(request):
    return render(request, 'event_create.html')

def list_events(request):
    if request.method == "POST":
        name = request.POST['name']
        datetime = dt.datetime.strptime(
            request.POST['datetime'], "%Y-%m-%d %H:%M:%S")
        location = request.POST['location']
        Event.objects.create(
            event_creator=request.user,
            name=name,
            datetime=datetime,
            location=location)
        
    events = Event.objects.all()
    ctx = {
        'title': 'Events list',
        'events': list(events),
    }
    return render(request, 'event_list.html', ctx)


def get_event(request, event_id : int):
    if request.method =='DELETE':
        Event.objects.filter(id=event_id).delete()
        
        return {}
        
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return HttpResponseNotFound('Event does not exists')
    ctx = { 'event': event }
    return render(request, 'event_details.html', ctx)