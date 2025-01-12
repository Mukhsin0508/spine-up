from django.contrib import admin
from .models import PostProduct, ClassDay, SessionStep, TwoPictures, TenPictures


class ClassDayInline(admin.TabularInline):
    """Inline admin for ClassDay model to allow admins to add/edit Product ClassDays."""
    model = ClassDay
    extra = 1

class SessionStepAdmin(admin.TabularInline):
    model = SessionStep
    extra = 6


class TwoPicturesInline(admin.TabularInline):
    """Inline admin for TwoPictures model to allow admins to add/edit Product TwoPictures."""
    model = TwoPictures
    extra = 2  # Assuming you want to show 2 picture slots


class TenPicturesInline(admin.TabularInline):
    """Inline admin for TenPictures model to allow admins to add/edit Product TenPictures."""
    model = TenPictures
    extra = 10  # Assuming you want to show 10 picture slots


@admin.register(PostProduct)
class PostProductAdmin(admin.ModelAdmin):
    """Admin panel configuration for the PostProduct model."""
    list_display = ('title', 'image', 'big_title', 'duration', 'number_of_sessions', 'description')
    search_fields = ('title', 'created_at')
    inlines = [ClassDayInline, TwoPicturesInline, TenPicturesInline, SessionStepAdmin]  # Enable inline editing for related models
