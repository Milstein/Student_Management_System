from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def student_home(request):
    return render(request,"student_management_system_app/student_template/student_home.html")