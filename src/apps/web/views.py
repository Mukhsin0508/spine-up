from rest_framework import generics

from .models import Staff, Certificate, CompanyCertificate
from .serializers import StaffSerializer, CertificateSerializer, CompanyCertificateSerializer


class StaffListView(generics.ListAPIView):
    """
    Retrieves a list of all Staff employees
    This view is accessible to all users browsing the Staffs
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class CertificateListView(generics.RetrieveAPIView):
    """
    Retrieves the corresponding certificate of the Staff
    This view is accessible to all the users browsing the Staffs with their Certificates
    """
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CompanyCertificateListView(generics.ListAPIView):
    """
    Retrieves the Company's Certificate.
    """
    queryset = CompanyCertificate.objects.all()
    serializer_class = CompanyCertificateSerializer