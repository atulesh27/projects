from django.contrib import admin
from .models import CourseInfoModel

# Register your models here.

class CourseInfoAdmin(admin.ModelAdmin):
    List_display = ['cname','cduration','cfess','cmentor']

admin.site.register(CourseInfoModel,CourseInfoAdmin)


