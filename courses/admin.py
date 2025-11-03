"""
Admin configuration for courses app.

Registers models in Django admin for easy management.
"""
from django.contrib import admin
from .models import Course, CourseDetail, CourseLead,ForWho,CoursePluses,CourseFAQ


class ForWhoInline(admin.TabularInline):
    model = ForWho
    
class CoursePlusesInline(admin.TabularInline):
    model = CoursePluses
    
class CourseFAQInline(admin.TabularInline):
    model = CourseFAQ


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin interface for Course model."""
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ForWhoInline, CoursePlusesInline, CourseFAQInline]


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    """Admin interface for CourseDetail model."""
    list_display = ['id', 'course', 'created_at']
    search_fields = ['course__title']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(CourseLead)
class CourseLeadAdmin(admin.ModelAdmin):
    """Admin interface for CourseLead model."""
    list_display = ['id', 'fullname', 'age', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['fullname', 'phone']
    readonly_fields = ['created_at']


@admin.register(ForWho)
class ForWhoAdmin(admin.ModelAdmin):
    """Admin interface for ForWho model."""
    list_display = ['id', 'course', 'for_who']
    list_filter = ['course']
    search_fields = ['course__title', 'for_who']


@admin.register(CoursePluses)
class CoursePlusesAdmin(admin.ModelAdmin):
    """Admin interface for CoursePluses model."""
    list_display = ['id', 'course', 'plus', 'created_at']
    list_filter = ['created_at']
    search_fields = ['course__title', 'plus']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(CourseFAQ)
class CourseFAQAdmin(admin.ModelAdmin):
    """Admin interface for CourseFAQ model."""
    list_display = ['id', 'course', 'question', 'created_at']
    list_filter = ['created_at']
    search_fields = ['course__title', 'question', 'answer']
    readonly_fields = ['created_at', 'updated_at']

