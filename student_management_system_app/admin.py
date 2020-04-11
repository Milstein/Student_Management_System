from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from student_management_system_app.models import CustomUser


class UserModel(UserAdmin):
    pass


admin.register(CustomUser, UserModel)

