from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Email
from datetime import date

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task()
def show():
    today = date.today()
    emails =Email.objects.filter(date__month=today.month)
    emails = list(emails)
    for mail in emails:
        logger.info(mail)