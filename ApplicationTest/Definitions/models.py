from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=200)

class JobPosting(models.Model):
    company = models.ForeignKey(Company, related_name="JobPosting", on_delete=models.CASCADE)
    jobposting_title = models.CharField(max_length=200)
    jobposting_description = models.TextField()

class Applicant(models.Model):
    jobposting = models.ForeignKey(JobPosting, related_name="Applicant", on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=200)
    applicant_email = models.CharField(max_length=200)
