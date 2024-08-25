from django.shortcuts import render

from django.views.generic import ListView

from .models import Event


class ListEventView(ListView):
    model = Event
    template_name = 'events/list_event.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.select_related('user').filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои события'
        context['user'] = self.request.user
        return context
