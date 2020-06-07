import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView

from student_management_system_app.models import Attendance, AttendanceReport, Course, CustomUser, FeedBackStaff, \
    LeaveReportStaff, SessionYear, Staff, Student, Subject, StudentResult


@login_required
def staff_home(request):
    # To fetch all Students Under Current Staff
    subjects = Subject.objects.filter(staff_id=request.user.id)
    course_id_list = []
    for subject in subjects:
        course = Course.objects.get(id=subject.course_id.id)
        course_id_list.append(course.id)

    # To get only unique Courses associated with Staff
    final_courses = set(course_id_list)

    total_students = Student.objects.filter(course_id__in=final_courses).count()

    # To fetch all Attendance Count
    attendance_count = Attendance.objects.filter(subject_id__in=subjects).count()

    # To fetch all Approved Leave Count
    staff = Staff.objects.get(admin=request.user.id)
    approved_leave_count = LeaveReportStaff.objects.filter(staff_id=staff.id).count()

    # Total Subjects Count
    total_subjects = subjects.count()

    # To fetch Attendance Data by Subject 
    subject_list = []
    present_attendance_by_subject_count_list = []
    absent_attendance_by_subject_count_list = []
    for subject in subjects:
        attendance = Attendance.objects.filter(subject_id=subject.id)        
        attendancereport_present_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=True).count()
        attendancereport_absent_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=False).count()
        if attendancereport_present_count > 0 or attendancereport_absent_count > 0:
            subject_list.append(subject.subject_name)
            present_attendance_by_subject_count_list.append(attendancereport_present_count)
            absent_attendance_by_subject_count_list.append(attendancereport_absent_count)

    # To fetch Attendance Data by Student
    students = Student.objects.filter(course_id__in=final_courses)
    student_list = []
    present_attendance_by_student_count_list = []
    absent_attendance_by_student_count_list = []
    for student in students:
        attendancereport_present_count = AttendanceReport.objects.filter(student_id=student.id, status=True).count()
        attendancereport_absent_count = AttendanceReport.objects.filter(student_id=student.id, status=False).count()
        if attendancereport_present_count > 0 or attendancereport_absent_count > 0:
            student_list.append(student.admin.get_full_name())
            present_attendance_by_student_count_list.append(attendancereport_present_count)
            absent_attendance_by_student_count_list.append(attendancereport_absent_count)

    context = {
        'total_students': total_students,
        'attendance_count': attendance_count,
        'approved_leave_count': approved_leave_count,
        'total_subjects': total_subjects,
        'subject_list': subject_list,
        'present_attendance_by_subject_count_list': present_attendance_by_subject_count_list,
        'absent_attendance_by_subject_count_list': absent_attendance_by_subject_count_list,
        'student_list': student_list,
        'present_attendance_by_student_count_list': present_attendance_by_student_count_list,
        'absent_attendance_by_student_count_list': absent_attendance_by_student_count_list
    }
    return render(request, "student_management_system_app/staff_template/staff_home.html", context)


@login_required
def staff_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staff.objects.get(admin=user)
    context = {
        'user': user,
        'staff': staff
    }
    return render(request, 'student_management_system_app/staff_template/staff_profile.html', context)


@login_required
def staff_profile_save(request):
    if request.method != 'POST':
        return redirect(reverse('student_management_system_app:staff_profile'))
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

            staff = Staff.objects.get(admin=user.id)
            staff.address = address
            staff.save()

            messages.success(request, "Successfully updated your profile.")
            return redirect(reverse('student_management_system_app:staff_profile'))
        except Exception as e:
            messages.error(request, "Failed To Update your profile Errors: {}".format(e))
            return redirect(reverse('student_management_system_app:staff_profile'))


@login_required
def take_attendance(request):
    context = {
        'subjects' : Subject.objects.filter(staff_id=request.user.id),
        'session_years' : SessionYear.objects.all()
    }
    return render(request, 'student_management_system_app/staff_template/take_attendance.html', context)


@csrf_exempt
def get_students(request):
    subject_id = request.POST.get('subject')
    session_year_id = request.POST.get('session_year')

    subject = Subject.objects.get(id=subject_id)
    session_year = SessionYear.objects.get(id=session_year_id)

    students = Student.objects.filter(course_id=subject.course_id, session_year_id=session_year)
    # student_data = serializers.serialize('python', students)
    list_data = []
    for student in students:
        data_small = { "id":student.admin.id, "name": student.admin.get_full_name() }
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def save_attendance_data(request):
    student_ids = request.POST.get('student_ids')
    subject_id = request.POST.get('subject_id')
    session_year_id = request.POST.get('session_year_id')
    attendance_date = request.POST.get('attendance_date')   

    subject_id = Subject.objects.get(id=subject_id)
    session_year_id = SessionYear.objects.get(id=session_year_id)

    json_student = json.loads(student_ids)
    
    try:
        attendance = Attendance(subject_id=subject_id, session_year_id = session_year_id, attendance_date=attendance_date)
        attendance.save()

        for student_info in json_student:
            student = Student.objects.get(admin=student_info['id'])
            attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=student_info['status'])
            attendance_report.save()

        return HttpResponse('OK')
    except:
        return HttpResponse('Error in saving Attendance Record!')


@login_required
def view_attendance_reports(request):
    attendances = AttendanceReport.objects.filter(attendance_id__subject_id__staff_id=request.user)
    return render(request, 'student_management_system_app/staff_template/view_attendance_reports.html', {"attendances":attendances})


@login_required
def edit_attendance(request):
    context = {
        'subjects' : Subject.objects.filter(staff_id=request.user),
        'session_years' : SessionYear.objects.all()
    }
    return render(request, 'student_management_system_app/staff_template/edit_attendance.html', context)


@csrf_exempt
def get_attendance_dates(request):
    subject_id = request.POST.get("subject")
    session_year_id = request.POST.get("session_year")
    subject = get_object_or_404(Subject, pk=subject_id)
    session_year = get_object_or_404(SessionYear, pk=session_year_id)

    attendances = Attendance.objects.filter(subject_id=subject, session_year_id=session_year)

    list_data = []
    for attendance in attendances:
        data_small = { "id":attendance.id, "session_year_id": attendance.session_year_id.id, "attendance_date": str(attendance.attendance_date) }
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def get_attendance_students(request):
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendancereports = AttendanceReport.objects.filter(attendance_id=attendance)

    list_data = []
    for attendancereport in attendancereports:
        data_small = { "id":attendancereport.student_id.admin.id, "name": attendancereport.student_id.admin.get_full_name(), "status": attendancereport.status }
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def update_attendance_data(request):
    student_ids = request.POST.get('student_ids')
    attendance_date = request.POST.get('attendance_date') 
    attendance = Attendance.objects.get(id=attendance_date)  
    json_student = json.loads(student_ids)
    
    try:
        for student_info in json_student:
            student = Student.objects.get(admin=student_info['id'])
            attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance)
            attendance_report.status = student_info['status']
            attendance_report.save()

        return HttpResponse('OK')
    except:
        return HttpResponse('Error in saving Attendance Record!')


class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name ='student_management_system_app/staff_template/take_attendance.html'
    fields = ['subject_id','session_year_id']
    # success_url = '/'

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request, "Successfully Taken Attendance")
        return redirect('student_management_system_app:take_attendance')


class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = Attendance
    template_name ='student_management_system_app/staff_template/edit_attendance.html'
    fields = ['subject_id', 'attendance_date', 'session_year_id']
    # success_url = '/'

    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Successfully Edited Attendance")
        # return redirect('student_management_system_app:view_attendance_reports')
        return redirect('student_management_system_app:edit_attendance', instance.pk)


class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'student_management_system_app/staff_template/delete_attendance.html'
    success_url = reverse_lazy('student_management_system_app:view_attendance_reports')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Successfully Deleted Attendance")
        return super().delete(self, request, *args, **kwargs)


@login_required
def staff_apply_leave(request):
    staff = Staff.objects.get(admin=request.user.id)
    leaves = LeaveReportStaff.objects.filter(staff_id=staff)
    return render(request, 'student_management_system_app/staff_template/staff_apply_leave.html', { 'leaves': leaves })


@login_required
def staff_leave_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        leave_date=request.POST.get("leave_date")
        leave_reason=request.POST.get("leave_reason")

        staff = Staff.objects.get(admin=request.user.id)
        try:
            leave = LeaveReportStaff(staff_id=staff, leave_date=leave_date,leave_reason=leave_reason)
            leave.save()
            messages.success(request,"Successfully Applied for a Leave")
            return redirect("student_management_system_app:staff_apply_leave")
        except Exception as e:
            messages.error(request,"Failed to Apply for a Leave {}".format(e))
            return redirect("student_management_system_app:staff_apply_leave")


@login_required
def staff_feedback(request):
    staff = Staff.objects.get(admin=request.user.id)
    feedbacks = FeedBackStaff.objects.filter(staff_id=staff)
    return render(request, 'student_management_system_app/staff_template/staff_feedback.html', { 'feedbacks': feedbacks })


@login_required
def staff_feedback_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        feedback_message=request.POST.get("feedback_message")

        staff = Staff.objects.get(admin=request.user.id)
        try:
            feedback = FeedBackStaff(staff_id=staff, feedback_message=feedback_message, feedback_reply="")
            feedback.save()
            messages.success(request,"Successfully Leave a Feedback Message")
            return redirect("student_management_system_app:staff_feedback")
        except Exception as e:
            messages.error(request,"Failed to Leave a Feedback Message {}".format(e))
            return redirect("student_management_system_app:staff_feedback")


@login_required
def staff_add_result(request):
    context = {
        'subjects' : Subject.objects.filter(staff_id=request.user.id),
        'session_years' : SessionYear.objects.all()
    }
    return render(request, 'student_management_system_app/staff_template/staff_add_result.html', context)


@login_required
def staff_save_student_result(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id = request.POST.get("subject")
        student_admin_id = request.POST.get("student_list")        
        exam_marks = request.POST.get("exam_marks")
        assignment_marks = request.POST.get("assignment_marks")        

        student = Student.objects.get(admin=student_admin_id)
        subject = Subject.objects.get(id=subject_id)
        try:
            check_exist = StudentResult.objects.filter(student_id=student, subject_id=subject).exists()
            if check_exist:
                result = StudentResult(student_id=student, subject_id=subject, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
                result.exam_marks = exam_marks
                result.assignment_marks = assignment_marks
                result.save()
                messages.success(request, 'Successfully Updated Student Result')
                return redirect(reverse("student_management_system_app:staff_add_result"))
            else:
                result = StudentResult(student_id=student, subject_id=subject, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
                result.save()
                messages.success(request, 'Successfully Added Student Result')
                return redirect(reverse("student_management_system_app:staff_add_result"))
        except Exception as e:
            messages.error(request,"Failed to Add Student Result {}".format(e))
            return redirect(reverse("student_management_system_app:staff_add_result"))