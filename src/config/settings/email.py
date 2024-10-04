import mimetypes
from django.core.mail import EmailMessage
from django.conf import settings

from config.validators import scan_file_for_viruses


def send_application_email(application):
    subject = f"New application for {application.vacancy.title} from {application.name}"
    message = f"""
    New Application received:
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

    if application.resume:
        # ==== Get the file name ====
        file_name = application.resume.name.split('/')[-1]
        file_path = application.resume.path

        # ==== Scan the uploaded resume ====
        scan_file_for_viruses(file_path)

        # Determine content type based on the file extension and encoding
        content_type, encoding = mimetypes.guess_type(file_name)
        if not content_type:
            # ===== Default to binary if type can't be guessed
            content_type = 'application/octet-stream'

        # ==== Attach the resume to the email ====
        email.attach(
            file_name,
            application.resume.read(),
            content_type
        )

    email.send()

