import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView

from student_management_system_app.models import Attendance, Subject, SessionYear, Student, AttendanceReport, \
    LeaveReportStaff, Staff, FeedBackStaff


@login_required
def staff_home(request):
    return render(request,"student_management_system_app/staff_template/staff_home.html")


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
        data_small = { "id":student.admin.id, "name": student.admin.first_name + ' ' + student.admin.last_name }
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
    attendances = AttendanceReport.objects.filter(status=True, attendance_id__subject_id__staff_id=request.user)
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
    print(list_data)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def get_attendance_students(request):
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendancereports = AttendanceReport.objects.filter(attendance_id=attendance)

    list_data = []
    for attendancereport in attendancereports:
        data_small = { "id":attendancereport.student_id.admin.id, "name": attendancereport.student_id.admin.first_name + ' ' + attendancereport.student_id.admin.last_name, "status": attendancereport.status }
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