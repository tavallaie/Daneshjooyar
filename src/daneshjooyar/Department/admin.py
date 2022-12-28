from django.contrib import admin
from Department.models import Department, Course, Chart

# Register your models here.
admin.site.register(Department)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ("dependencies",)


@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)
