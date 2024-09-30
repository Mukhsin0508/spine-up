from django.contrib import admin
from .models import PostVacancy, JobRequirement, Application

# Inline admin for JobRequirement model to be displayed within the PostVacancy admin panel.
class JobRequirementInline(admin.TabularInline):
    """
    Inline admin for JobRequirement model to allow admins to add/edit job requirements
    directly when creating or editing a PostVacancy.
    """
    model = JobRequirement
    extra = 1


@admin.register(PostVacancy)
class PostVacancyAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for the PostVacancy model, allowing admins to manage job vacancies.
    """
    list_display = ('title', 'salary_from', 'salary_to', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    inlines = [JobRequirementInline]  # Enable inline editing of job requirements when creating or editing a vacancy.


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for the Application model.
    Admins can view all applications and filter them by the associated vacancy.
    """
    list_display = ('name', 'vacancy', 'phone_number', 'created_at')
    list_filter = ('vacancy',)  # Allow filtering of applications by job vacancy.
    search_fields = ('name', 'phone_number')
