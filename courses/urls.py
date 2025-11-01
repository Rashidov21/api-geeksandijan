"""
URL configuration for courses app.

Defines URL patterns for course-related API endpoints.
"""
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # List all courses
    path('courses/', views.CourseListView.as_view(), name='course-list'),
    # Get single course by ID
    path('courses/<int:id>/', views.CourseDetailView.as_view(), name='course-detail'),
    # Create new course lead (public - anyone can submit)
    path('leads/', views.CourseLeadCreateView.as_view(), name='course-lead-create'),
    # List all course leads (admin only - requires staff privileges)
    path('leads/admin/', views.CourseLeadListView.as_view(), name='course-lead-list'),
]

