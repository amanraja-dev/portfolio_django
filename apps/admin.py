from django.contrib import admin
from .models import Profile, Social, Project, ProjectImage, Language, Frontend, Backend, Database, TenthDetails, TwelfthDetails, CollegeDetails, Feedback, Resume, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'designation', 'created', 'updated']
    search_fields = ['user__username', 'designation']

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'created', 'updated']
    search_fields = ['user__username', 'name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'created', 'updated']
    search_fields = ['name', 'user__username']

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'image']
    search_fields = ['project__name']

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Frontend)
class FrontendAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Backend)
class BackendAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(Database)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(TenthDetails)
class TenthDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'school_name', 'year_of_passing', 'percentage', 'created', 'updated']
    search_fields = ['user__username', 'school_name']

@admin.register(TwelfthDetails)
class TwelfthDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'school_name', 'year_of_passing', 'percentage', 'created', 'updated']
    search_fields = ['user__username', 'school_name']

@admin.register(CollegeDetails)
class CollegeDetailsAdmin(admin.ModelAdmin):
    list_display = ['user', 'college_name', 'degree', 'field_of_study', 'year_of_graduation', 'created', 'updated']
    search_fields = ['user__username', 'college_name']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile', 'gmail', 'created_at']
    search_fields = ['name', 'gmail']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['user', 'qualification', 'institute_name', 'percentage', 'passing_year', 'created_at', 'updated_at']