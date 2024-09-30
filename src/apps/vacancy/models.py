from django.db import models
from django.core.validators import FileExtensionValidator
from config.validators import phone_validate


class PostVacancy(models.Model):
    """Model representing a job vacancy post."""
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=500)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class JobRequirement(models.Model):
    """Model representing the specific requirements for a job vacancy."""
    vacancy = models.ForeignKey(PostVacancy, on_delete=models.CASCADE, related_name='requirements')
    requirement = models.TextField()

    def __str__(self):
        return f"Requirements for {self.vacancy.title}"


class Application(models.Model):
    """Model representing an application submitted by a candidate for a specific job vacancy."""
    vacancy = models.ForeignKey(PostVacancy, on_delete=models.CASCADE, related_name='applications')
    name = models.CharField(max_length=100)
    experience = models.TextField()
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]
        )
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.vacancy.title} by {self.name}"