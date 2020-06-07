from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from student_management_system_app.models import Student, Subject, Attendance, AttendanceReport, \
    LeaveReportStudent, FeedBackStudent, CustomUser, Course, NotificationStudent


@login_required
def student_home(request):
    student = Student.objects.get(admin = request.user.id)
    total_attendance = AttendanceReport.objects.filter(student_id=student).count()
    presence_attendance = AttendanceReport.objects.filter(student_id=student, status=True).count()
    absence_attendance = AttendanceReport.objects.filter(student_id=student, status=False).count()
    course = Course.objects.get(id = student.course_id.id)
    total_subjects = Subject.objects.filter(course_id = course).count()

    subject_names = []
    present_data = []
    absent_data = []
    subjects = Subject.objects.filter(course_id=student.course_id)
    for subject in subjects:
        attendance = Attendance.objects.filter(subject_id=subject.id)
        attendace_present_count = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=student, status=True).count()
        attendace_absent_count = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=student, status=False).count()
        subject_names.append(subject.subject_name)
        present_data.append(attendace_present_count)
        absent_data.append(attendace_absent_count)
    context = {
        'total_attendance': total_attendance,
        'presence_attendance': presence_attendance,
        'absence_attendance': absence_attendance,
        'total_subjects': total_subjects,
        'subject_names' : subject_names,
        'present_data' : present_data,
        'absent_data' : absent_data
    }
    return render(request,"student_management_system_app/student_template/student_home.html", context)


@login_required
def student_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Student.objects.get(admin=user)
    context = {
        'user': user,
        'student': student
    }
    return render(request, 'student_management_system_app/student_template/student_profile.html', context)


@login_required
def student_profile_save(request):
    if request.method != 'POST':
        return redirect(reverse('student_management_system_app:student_profile'))
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            if password is not None and password != "":
                user.set_password(password)
            user.save()

            student = Student.objects.get(admin=user.id)
            student.address = address
            student.save()

            messages.success(request, "Successfully updated your profile.")
            return redirect(reverse('student_management_system_app:student_profile'))
        except Exception as e:
            messages.error(request, "Failed To Update your profile Errors: {}".format(e))
            return redirect(reverse('student_management_system_app:student_profile'))


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


@csrf_exempt
def student_fcm_token_save(request):
    try:
        token = request.POST.get('token')
        student = Student.objects.get(admin=request.user.id)
        student.fcm_token = token
        student.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')


def student_all_notifications(request):
    student = Student.objects.get(admin=request.user.id)
    notifications = NotificationStudent.objects.filter(student_id=student.id).order_by('-created_at')
    return render(request, 'student_management_system_app/student_template/all_notifications.html',
                  {'notifications': notifications})
