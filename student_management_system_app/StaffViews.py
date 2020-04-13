from django.shortcuts import render


def staff_home(request):
    return render(request,"student_management_system_app/staff_template/staff_home.html")