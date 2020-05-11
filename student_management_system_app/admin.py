from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_system_app.models import CustomUser


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

# Customizing the admin texts
admin.site.site_header = "Student Management System"
admin.site.index_title = "Welcome to project"
admin.site.site_title = "Control Panel"