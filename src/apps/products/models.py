from django.db import models
from multiselectfield import MultiSelectField


class PostProduct(models.Model):
    title = models.TextField(max_length=150)
    description = models.TextField(max_length=300)
    number_of_sessions = models.CharField(max_length=3)
    duration = models.CharField(max_length=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ClassDay(models.Model):
    WEEK_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    product = models.ForeignKey(PostProduct, on_delete=models.CASCADE, related_name='class_days')
    days = MultiSelectField(max_length=50, choices=WEEK_CHOICES, max_choices=3)

    def __str__(self):
        return f"Class days for {self.product.title}: {','.join(self.days)}"

