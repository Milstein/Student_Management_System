from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from student_management_system_app.models import Student, Course, Subject, Attendance, AttendanceReport


@login_required
def student_home(request):
    return render(request,"student_management_system_app/student_template/student_home.html")


def student_view_attendance(request):
    student = Student.objects.get(admin=request.user.id)
    subjects = Subject.objects.filter(course_id=student.course_id)
    context = {
        'subjects': subjects
    }
    return render(request, "student_management_system_app/student_template/student_view_attendance.html", context)


def view_student_attendance_data(request):
    student = Student.objects.get(admin=request.user.id)
    subject_id = request.POST.get('subject')
    subject = Subject.objects.get(id=subject_id)
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    start_date_parse = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_parse = datetime.strptime(end_date, '%Y-%m-%d').date()

    attendance = Attendance.objects.filter(attendance_date__range=(start_date_parse, end_date_parse), subject_id=subject)
    attendace_reports = AttendanceReport.objects.filter(student_id=student.id, attendance_id__in=attendance)

    # for attendace_report in attendace_reports:
    #     print('Date : ' + str(attendace_report.attendance_id.attendance_date) + ' Status: ' + str(attendace_report.status))
    context = {
        'attendace_reports': attendace_reports
    }
    return render(request, "student_management_system_app/student_template/student_attendance_data.html", context)
