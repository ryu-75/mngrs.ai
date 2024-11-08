from django.core.mail import send_mail
import logging


logger = logging.getLogger(__name__)

class EmailService:
    @staticmethod
    def send_project_created_email(recipient_email: str):
        try:
            subject = 'Project created'
            message = 'You have created a new project.'
            from_email = 'test@example.com'
            send_mail(subject, message, from_email, [recipient_email])
            logger.info('Email sent successfully to %s', recipient_email)
        except Exception as e:
            logger.error(f'Error sending email to %s: %s', recipient_email, e)
            raise e