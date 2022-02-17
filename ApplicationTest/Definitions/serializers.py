from rest_framework import serializers
from TestSite.models import Company, JobPosting, Applicant

class CompanySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Company
        fields = ['url', 'id', 'company_name']

class JobPostingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JobPosting
        fields = ['url', 'id', 'company', 'jobposting_title', 'jobposting_description']

class ApplicantSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Applicant
        fields = ['url', 'id', 'jobposting', 'applicant_name', 'applicant_email']