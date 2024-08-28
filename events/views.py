from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.http import HttpResponseRedirect

from django.views.generic import ListView

from .tasks import send_event_list_to_email

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


class SendEventListView(View):
    def post(self, request, *args, **kwargs):
        user_email = request.user.email
        send_event_list_to_email.delay(user_email)
        messages.info(request, "Ваше обращение в работе. В течение 5 минут файл будет у вас на почте.")
        return HttpResponseRedirect(reverse('list_event'))
