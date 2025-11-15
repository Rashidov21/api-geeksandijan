"""
Views for the courses app.

This module defines class-based views using DRF generics for
listing, retrieving courses, and creating course leads.
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Course, CourseLead
from .serializers import CourseSerializer, CourseLeadSerializer


class CourseListView(generics.ListAPIView):
    """
    ListAPIView for retrieving all courses.

    Returns a list of all courses with their details (if available).
    Each course includes nested information from ForWho, CoursePluses,
    CourseFAQ, and CourseDetail.
    """
    queryset = Course.objects.all().prefetch_related('forwho_set', 'coursepluses_set', 'coursefaq_set').select_related('details')
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    """
    RetrieveAPIView for getting a single course with details.

    Returns a single course by ID with all its details including
    nested information from ForWho, CoursePluses, CourseFAQ, and CourseDetail.
    
    This endpoint is publicly accessible and returns comprehensive course information
    including target audience, pluses, FAQs, and legacy course details.
    """
    queryset = Course.objects.all().prefetch_related(
        'forwho_set', 
        'coursepluses_set', 
        'coursefaq_set'
    ).select_related('details')
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]  # Public access
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve method to provide custom response handling.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CourseLeadCreateView(generics.CreateAPIView):
    """
    CreateAPIView for posting new course leads.

    Accepts POST requests with course, fullname, age, and phone to create
    a new course lead. Returns the created lead with status 201.
    This endpoint is publicly accessible (AllowAny).
    """
    queryset = CourseLead.objects.all()
    serializer_class = CourseLeadSerializer
    permission_classes = [AllowAny]  # Explicitly allow unauthenticated users

    def create(self, request, *args, **kwargs):
        """
        Override create method to return custom response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class CourseLeadListView(generics.ListAPIView):
    """
    ListAPIView for retrieving all course leads.

    Returns a list of all course leads. This endpoint is restricted
    to admin users only (IsAdminUser). Regular users will get 403 Forbidden.
    """
    queryset = CourseLead.objects.all().select_related('course')
    serializer_class = CourseLeadSerializer
    permission_classes = [IsAdminUser]  # Only staff/admin users can access

