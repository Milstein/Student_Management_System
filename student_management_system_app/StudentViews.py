from django.shortcuts import render


def student_home(request):
    return render(request,"student_management_system_app/student_template/student_home.html")