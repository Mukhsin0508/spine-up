from rest_framework import serializers
from .models import Staff, Certificate, CompanyCertificate



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'title', 'image', 'date_issued']

class StaffSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'name', 'position', 'years_of_experience', 'certificates']


class CompanyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCertificate
        fields = ['id', 'title', 'image']
