from django.contrib import admin
from .models import PostProduct, ClassDay

# Inline class for ClassDay model to be displayed within the Product admin panel.
class ClassDayInline(admin.TabularInline):
    """
    Inline admin for ClassDay model to allow admins to add/edit Product ClassDays
    directly when creating or editing a Product.
    """
    model = ClassDay
    extra = 1  # Number of extra inline forms to display


@admin.register(PostProduct)
class PostProductAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the PostProduct model, including the ClassDayInline.
    """
    list_display = ('title', 'image', 'duration', 'number_of_sessions', 'description')
    search_fields = ('title', 'created_at')
    inlines = [ClassDayInline] # Enable inline editing of Product ClassDays when creating or editing a Product.



