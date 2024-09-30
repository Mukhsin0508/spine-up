from django.urls import path
from .views import PostVacancyListView, PostVacancyDetailView, ApplicationCreateView


urlpatterns = [
    path('vacancies/', PostVacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', PostVacancyDetailView.as_view(), name='vacancy-detail'),
    path('applications/', ApplicationCreateView.as_view(), name='application-create'),

    ]