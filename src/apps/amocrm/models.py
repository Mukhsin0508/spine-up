from django.utils import timezone

from django.db import models
from config.validators import phone_validate

class ClientData(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, validators=[phone_validate])  # Updated max_length
    service = models.CharField(max_length=20, null=True, blank=True)
    platform = models.CharField(max_length=15, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_created_at(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
