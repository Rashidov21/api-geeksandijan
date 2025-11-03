"""
Admin configuration for courses app.

Registers models in Django admin for easy management.
"""
from django.contrib import admin
from .models import Course, CourseDetail, CourseLead,ForWho,CoursePluses


class ForWhoInline(admin.TabularInline):
    model = ForWho
    
class CoursePlusInline(admin.TabularInline):
    model = CoursePluses

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin interface for Course model."""
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ForWhoInline, CoursePlusInline]


    

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

