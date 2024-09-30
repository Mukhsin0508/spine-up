from rest_framework import serializers
from .models import PostVacancy, JobRequirement, Application

class JobRequirementSerializer(serializers.ModelSerializer):
    """This serializer is used to represent individual job requirements."""
    class Meta:
        model = JobRequirement
        fields = ['requirement'] # Only the requirement field is exposed.

class PostVacancySerializer(serializers.ModelSerializer):
    """Serializer for PostVacancy model, which also handles nested JobRequirements."""
    requirements = JobRequirementSerializer(many=True, required=False)

    class Meta:
        model = PostVacancy
        fields = ['id', 'title', 'description', 'salary_to', 'salary_from', 'created_at', 'updated_at', 'requirements']

    # ======== Custom create method to handle nested requirements during vacancy creation. ========
    def create(self, validated_data):
        requirements_data = validated_data.pop('requirements', [])
        vacancy = PostVacancy.objects.create(**validated_data)

        # ======== Create each JobRequirement associated with the created vacancy.  ========
        for requirements_data in requirements_data:
            JobRequirement.objects.create(vacancy=vacancy, **requirements_data)
        return vacancy

class ApplicationSerializer(serializers.ModelSerializer):
    """Used to handle serialization of job applications."""
    class Meta:
        model = Application
        fields = ['id', 'vacancy', 'name', 'experience', 'resume', 'phone_number', 'created_at']

