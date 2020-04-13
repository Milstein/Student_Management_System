from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def staff_home(request):
    return render(request,"student_management_system_app/staff_template/staff_home.html")