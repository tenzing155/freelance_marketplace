from django.urls import path
from django.http import JsonResponse
from .views import JobListCreateView, JobDetailView, create_checkout_session

def get_jobs(request):
    jobs = [
        {"id": 1, "title": "Web Developer", "budget": 500},
        {"id": 2, "title": "Graphic Designer", "budget": 300},
    ]
    return JsonResponse(jobs, safe=False)

urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('sample-jobs/', get_jobs, name='sample-jobs'),  # Changed the path to avoid conflict
]
