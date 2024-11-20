from django.db import models
from multiselectfield import MultiSelectField

from config.validators import validate_product_image


class PostProduct(models.Model):
    title = models.TextField(max_length=150)
    image = models.ImageField(upload_to='post-images', validators=[validate_product_image], blank=True, null=True)
    description = models.TextField(max_length=300)
    big_title = models.TextField(max_length=200)
    big_description = models.TextField(max_length=600, blank=True, null=True)
    number_of_sessions = models.CharField(max_length=3)
    duration = models.CharField(max_length=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TwoPictures(models.Model):
    product = models.ForeignKey(PostProduct, on_delete=models.CASCADE, related_name='two_pictures')
    image = models.ImageField(upload_to='post-images/two-pictures', validators=[validate_product_image])

    def __str__(self):
        return f"Image for {self.product.title} (Two Pictures)"


class TenPictures(models.Model):
    product = models.ForeignKey(PostProduct, on_delete=models.CASCADE, related_name='ten_pictures')
    image = models.ImageField(upload_to='post-images/ten-pictures', validators=[validate_product_image])

    def __str__(self):
        return f"Image for {self.product.title} (Ten Pictures)"


class ClassDay(models.Model):
    WEEK_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота'),
        ('Воскресенье', 'Воскресенье'),
    )

    product = models.ForeignKey(PostProduct, on_delete=models.CASCADE, related_name='class_days')
    days = MultiSelectField(max_length=50, choices=WEEK_CHOICES)

    def __str__(self):
        return f"Class days for {self.product.title}: {', '.join(self.days)}"
