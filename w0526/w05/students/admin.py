from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','major','grade']


# Register your models here.

admin.site.register(Student,StudentAdmin)