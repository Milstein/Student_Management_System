from datetime import datetime
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from student_management_system_app.models import Student, Course, Subject, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent


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

    context = {
        'attendace_reports': attendace_reports
    }
    return render(request, "student_management_system_app/student_template/student_attendance_data.html", context)


@login_required
def student_apply_leave(request):
    student = Student.objects.get(admin=request.user.id)
    leaves = LeaveReportStudent.objects.filter(student_id=student)
    return render(request, 'student_management_system_app/student_template/student_apply_leave.html', { 'leaves': leaves })


@login_required
def student_leave_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        leave_date=request.POST.get("leave_date")
        leave_reason=request.POST.get("leave_reason")

        student = Student.objects.get(admin=request.user.id)
        try:
            leave = LeaveReportStudent(student_id=student, leave_date=leave_date,leave_reason=leave_reason)
            leave.save()
            messages.success(request,"Successfully Applied for a Leave")
            return redirect("student_management_system_app:student_apply_leave")
        except Exception as e:
            messages.error(request,"Failed to Apply for a Leave {}".format(e))
            return redirect("student_management_system_app:student_apply_leave")


@login_required
def student_feedback(request):
    student = Student.objects.get(admin=request.user.id)
    feedbacks = FeedBackStudent.objects.filter(student_id=student)
    return render(request, 'student_management_system_app/student_template/student_feedback.html', { 'feedbacks': feedbacks })


@login_required
def student_feedback_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        feedback_message=request.POST.get("feedback_message")

        student = Student.objects.get(admin=request.user.id)
        try:
            feedback = FeedBackStudent(student_id=student, feedback_message=feedback_message, feedback_reply="")
            feedback.save()
            messages.success(request,"Successfully Leave a Feedback Message")
            return redirect("student_management_system_app:student_feedback")
        except Exception as e:
            messages.error(request,"Failed to Leave a Feedback Message {}".format(e))
            return redirect("student_management_system_app:student_feedback")