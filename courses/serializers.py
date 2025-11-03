"""
Serializers for the courses app.

This module defines DRF serializers for Course, CourseDetail, and CourseLead models.
CourseSerializer includes nested serializers for related models (read-only).
"""
from rest_framework import serializers
from .models import Course, CourseDetail, CourseLead, ForWho, CoursePluses, CourseFAQ


class ForWhoSerializer(serializers.ModelSerializer):
    """
    Serializer for ForWho model.

    Used as a nested serializer within CourseSerializer.
    """
    class Meta:
        model = ForWho
        fields = ['id', 'for_who']
        read_only_fields = ['id']


class CoursePlusesSerializer(serializers.ModelSerializer):
    """
    Serializer for CoursePluses model.

    Used as a nested serializer within CourseSerializer.
    """
    class Meta:
        model = CoursePluses
        fields = ['id', 'plus', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseFAQSerializer(serializers.ModelSerializer):
    """
    Serializer for CourseFAQ model.

    Used as a nested serializer within CourseSerializer.
    """
    class Meta:
        model = CourseFAQ
        fields = ['id', 'question', 'answer', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for CourseDetail model.

    Used as a nested serializer within CourseSerializer.
    """
    class Meta:
        model = CourseDetail
        fields = ['pluses', 'inthis_course']
        read_only_fields = ['pluses', 'inthis_course']


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course model.

    Includes nested serializers for related models (read-only):
    - ForWho: target audience for the course
    - CoursePluses: advantages of the course
    - CourseFAQ: frequently asked questions
    - CourseDetail: legacy details (if available)
    """
    for_who_list = ForWhoSerializer(many=True, read_only=True, source='forwho_set')
    pluses_list = CoursePlusesSerializer(many=True, read_only=True, source='coursepluses_set')
    faqs = CourseFAQSerializer(many=True, read_only=True, source='coursefaq_set')
    details = CourseDetailSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'for_who_list', 'pluses_list', 'faqs', 'details', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CourseLeadSerializer(serializers.ModelSerializer):
    """
    Serializer for CourseLead model.

    Used for creating new course leads.
    """
    class Meta:
        model = CourseLead
        fields = ['id', 'fullname', 'age', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_phone(self, value):
        """
        Validate phone number format.

        Basic validation to ensure phone number is not empty.
        Add more complex validation as needed.
        """
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Phone number cannot be empty.")
        return value.strip()

    def validate_age(self, value):
        """
        Validate age is within reasonable range.
        """
        if value < 1 or value > 150:
            raise serializers.ValidationError("Age must be between 1 and 150.")
        return value

