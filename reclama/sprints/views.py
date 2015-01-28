from django.shortcuts import render

from reclama.sprints.models import Event, Bug


def home(request):
    events = Event.objects.filter(archived=False)
    return render(request, 'index.html', {'events': events})


def event(request, slug):
    """Render event bugs."""
    event = Event.objects.get(slug=slug)

    bugs = Bug.objects.filter(event=event)

    return render(request, 'bugs.html',
                  {'open': not event.archived,
                   'event': event,
                   'bugs': bugs})
