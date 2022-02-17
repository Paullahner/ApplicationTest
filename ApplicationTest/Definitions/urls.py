from rest_framework.urlpatterns import format_suffix_patterns
from TestSite.views import CompanyViewSet, JobPostingViewSet, ApplicantViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Companies', CompanyViewSet)
router.register(r'JobPostings', JobPostingViewSet)
router.register(r'Applicant', ApplicantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

jobposting_list = JobPostingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
jobpostig_detail = JobPostingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

applicant_list = ApplicantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
applicant_detail = ApplicantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('companies/', company_list, name='company-list'),
    path('companies/<int:pk>/', company_detail, name='company-detail'),
    path('jobpostings/', jobposting_list, name='jobposting-list'),
    path('jobpostings/<int:pk>/', jobpostig_detail, name='jobposting-detail'),
    path('applicants/', applicant_list, name='applicant-list'),
    path('applicants/<int:pk>/', applicant_detail, name='applicant-detail')
])