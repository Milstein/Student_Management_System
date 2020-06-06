from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_system_app.AdminViews":
                    pass
                elif modulename == "student_management_system_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect('student_management_system_app:admin_home')
            elif user.user_type == "2":
                if modulename == "student_management_system_app.StaffViews":
                    pass
                elif modulename == "student_management_system_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect('student_management_system_app:staff_home')
            elif user.user_type == "3":
                if modulename == "student_management_system_app.StudentViews":
                    pass
                elif modulename == "student_management_system_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect('student_management_system_app:student_home')
            else:
                return redirect('student_management_system_app:login_user')
        else:
            if request.path == reverse("student_management_system_app:home") or request.path == reverse("student_management_system_app:signup") or request.path == reverse("student_management_system_app:login_user") or modulename == "django.contrib.auth.views":
                pass
            else:
                return redirect('student_management_system_app:home')