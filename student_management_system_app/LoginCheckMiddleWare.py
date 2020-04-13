from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_system_app.AdminViews":
                    pass
                elif modulename == "student_management_system_app.views":
                    pass
                else:
                    return redirect('student_management_system_app:admin_home')
            elif user.user_type == "2":
                if modulename == "student_management_system_app.StaffViews":
                    pass
                elif modulename == "student_management_system_app.views":
                    pass
                else:
                    return redirect('student_management_system_app:staff_home')
            elif user.user_type == "3":
                if modulename == "student_management_system_app.StudentViews":
                    pass
                elif modulename == "student_management_system_app.views":
                    pass
                else:
                    return redirect('student_management_system_app:student_home')
            else:
                return redirect('student_management_system_app:login_user')
        # else:
        #     if request.path == reverse("student_management_system_app:home") or request.path == reverse("student_management_system_app:show_login") or request.path == reverse("student_management_system_app:login_user"):
        #         pass
        #     else:
        #         return redirect('student_management_system_app:home')