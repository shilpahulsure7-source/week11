from django.shortcuts import render


def event_home(request):
    return render(request, 'events/events.html')