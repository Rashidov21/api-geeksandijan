"""
Models for the courses app.

This module defines the Course, CourseDetail, and CourseLead models
for the Geeks Andijan courses API.
"""
from django.db import models


class Course(models.Model):
    """
    Main course model.

    Represents a course offered by Geeks Andijan with basic information
    about title, description, and target audience.
    """
    # Choices for the 'for_who' field
    TARGET_AUDIENCE_CHOICES = [
        ('beginners', 'Beginners'),
        ('students', 'Students'),
        ('professionals', 'Professionals'),
    ]

    title = models.CharField(
        max_length=200,
        help_text="Course title"
    )
    description = models.TextField(
        help_text="Detailed course description"
    )
    for_who = models.CharField(
        max_length=20,
        choices=TARGET_AUDIENCE_CHOICES,
        help_text="Target audience for this course"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title


class CourseDetail(models.Model):
    """
    Detailed information about a course.

    This model has a OneToOne relationship with Course and stores
    additional details like pluses and course content (inthis_course).
    """
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name='details',
        help_text="Related course"
    )
    pluses = models.JSONField(
        default=list,
        help_text="List of course advantages (e.g., ['mentor', 'project', 'team', 'certificate'])"
    )
    inthis_course = models.JSONField(
        default=list,
        help_text="List of objects with question and answer about course content"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Course Detail'
        verbose_name_plural = 'Course Details'

    def __str__(self):
        return f"Details for {self.course.title}"


class CourseLead(models.Model):
    """
    Lead model for course inquiries.

    Stores information about potential students who are interested
    in courses (name, age, phone number).
    """
    fullname = models.CharField(
        max_length=100,
        help_text="Full name of the lead"
    )
    age = models.PositiveIntegerField(
        help_text="Age of the lead"
    )
    phone = models.CharField(
        max_length=20,
        help_text="Phone number of the lead"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Course Lead'
        verbose_name_plural = 'Course Leads'

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

