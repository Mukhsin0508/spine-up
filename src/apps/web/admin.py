from django.contrib import admin
from .models import Staff, Certificate, CompanyCertificate

class CertificateInline(admin.StackedInline):
    model = Certificate
    extra = 1


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    inlines = [CertificateInline]

admin.site.register(CompanyCertificate)