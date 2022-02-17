from TestSite.models import Company, JobPosting, Applicant
from TestSite.serializers import CompanySerializer, JobPostingSerializer, ApplicantSerializer
from rest_framework import viewsets

class CompanyViewSet(viewsets.ModelViewSet):

    queryset = Company.objects.all()
    serializer_class =CompanySerializer

class JobPostingViewSet(viewsets.ModelViewSet):

    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class ApplicantViewSet(viewsets.ModelViewSet):

    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer