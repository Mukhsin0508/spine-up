from django.urls import path
from .views import StaffListView, CertificateListView, CompanyCertificateListView

urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff'),
    path('certificate/', CertificateListView.as_view(), name='certificate'),
    path('company-certificate', CompanyCertificateListView.as_view(), name='company-certificate')
    ]