from django.contrib import admin
from gallary.students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'ZhongDui', 'QuDui')

admin.site.register(Student, StudentAdmin)