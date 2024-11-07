from django.db import models
from multiselectfield import MultiSelectField

from config.validators import validate_product_image


class PostProduct(models.Model):
    title = models.TextField(max_length=150)
    image = models.ImageField(upload_to='post-images', validators=[validate_product_image], blank=True, null=True)
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
    days = MultiSelectField(max_length=50, choices=WEEK_CHOICES)

    def __str__(self):
        return f"Классные дни для {self.product.title}: {','.join(self.days)}"

