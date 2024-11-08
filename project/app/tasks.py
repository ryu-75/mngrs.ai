from celery import shared_task
from app.services import EmailService
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_email_task():
    try:
        EmailService.send_project_created_email('recipient@example.com')
        logger.info('Email sent successfully')
    except Exception as e:
        logger.error(f'Error sending email: {e}')
    return 'Email sent successfully'