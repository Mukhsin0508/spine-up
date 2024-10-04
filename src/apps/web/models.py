from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    years_of_experience = models.CharField()

    def __str__(self):
        return self.name


class Certificate(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    date_issued = models.DateField()
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return f"{self.staff.name} - {self.title}"
    

class CompanyCertificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='company_certificates/')

    def __str__(self):
        return self.title

