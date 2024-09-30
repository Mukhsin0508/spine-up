from rest_framework import generics

from .models import PostVacancy
from .serializers import PostVacancySerializer, ApplicationSerializer
from config.settings.email import send_application_email



class PostVacancyListView(generics.ListAPIView):
    """
    Retrieves a list of all job vacancies.
    This view is accessible to all users for browsing job openings.
    """
    queryset = PostVacancy.objects.all()
    serializer_class = PostVacancySerializer


class PostVacancyDetailView(generics.RetrieveAPIView):
    """
    Retrieves the details of a specific job vacancy.
    This view allows users to view detailed information about a particular vacancy.
    """
    queryset = PostVacancy.objects.all()
    serializer_class = PostVacancySerializer


class ApplicationCreateView(generics.CreateAPIView):
    """
    Allows users to submit a job application.
    This view handles the job application submission and sends an email notification
    when a new application is created.
    """
    serializer_class = ApplicationSerializer

    def perform_create(self, serializer):
        # Save the application and send an email notification.
        application = serializer.save()
        send_application_email(application)
