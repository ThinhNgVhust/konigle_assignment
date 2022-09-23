from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Email
from datetime import date

@shared_task()
def show():
    today = date.today()
    emails = Email.objects.filter(date__month=today.month)
    print("The number of new emails added in this month:",len(emails))