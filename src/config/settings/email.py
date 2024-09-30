from django.core.mail import EmailMessage
from django.conf import settings


def send_application_email(application):
    subject = f"New application for {application.vacancy.title}"
    message = f"""
    New Application recieved:
    Name: {application.name}
    Phone: {application.phone_number}
    Experience: {application.experience}
    """

    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HR_USER]
        )
    email.attach(application.resume.name, application.resume.read(), application.resume.content_type)
    email.send()

