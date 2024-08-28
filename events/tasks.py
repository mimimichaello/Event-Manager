from celery import shared_task
from django.core.mail import EmailMessage
from openpyxl import Workbook
from .models import Event
from django.utils.timezone import make_naive

@shared_task
def send_event_list_to_email(user_email):
    events = Event.objects.filter(user__email=user_email)

    wb= Workbook()
    ws = wb.active
    ws.title = 'Список событий'


    ws.append(['Название', 'Описание', 'Дата', 'Статус', 'Место'])

    for event in events:
        event_date = make_naive(event.date) if event.date else None
        ws.append([event.title, event.description, event_date, event.status, event.location])

    filepath = "/tmp/events_list.xlsx"
    wb.save(filepath)

    email = EmailMessage(
        subject='Ваш список событий',
        body='В приложении прилагается список ваших событий.',
        to=[user_email]
    )
    email.attach_file(filepath)
    email.send()
