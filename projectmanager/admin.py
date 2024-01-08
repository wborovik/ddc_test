from django.contrib import admin
from .models import Project, Task, Employee


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_manager', 'is_active')
    list_filter = ['project_manager', 'is_active']
    list_per_page = 10


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'deadline', 'employee', 'status')
    list_editable = ('deadline', 'employee', 'status')
    list_filter = ['project__title', 'status', 'employee']
    list_per_page = 10


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', 'job_title')
    list_display_links = ('last_name', 'first_name', 'patronymic')
    list_filter = ['job_title']
    list_per_page = 10
