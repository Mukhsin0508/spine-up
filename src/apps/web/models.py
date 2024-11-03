from django.db import models

from config.validators import validate_staff_image


class Staff(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='staff_images', null=True, blank=True, validators=[validate_staff_image])
    position = models.CharField(max_length=100)
    years_of_experience = models.CharField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200, blank=True, null=True)
    date_issued = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"{self.staff.name} - {self.title}"
    

class CompanyCertificate(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='company_certificates/')

    def __str__(self):
        return self.title

