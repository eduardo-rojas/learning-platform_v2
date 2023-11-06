from django.contrib import admin
from .models import Subject, Course, Module 

# Register to admin site: Subject Model
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

# Register to admin site: Module Model
class ModuleInline(admin.StackedInline):
    model = Module 

# Register to admin site: Course Model
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter =  ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

