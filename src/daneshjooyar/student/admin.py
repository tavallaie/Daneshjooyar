from django.contrib import admin
from student.models import StudentProfile, Terms

# Register your models here.


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)


admin.site.register(StudentProfile)
