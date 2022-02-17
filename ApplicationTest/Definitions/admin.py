from django.contrib import admin
from .models import Company, JobPosting, Applicant

admin.site.register(Company)

admin.site.register(JobPosting)

admin.site.register(Applicant)

# Register your models here.
