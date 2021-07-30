from django.contrib import admin
from .models import * 

# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','entryPeriod')

admin.site.register(Students, StudentsAdmin)
