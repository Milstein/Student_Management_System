import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView, DeleteView

from student_management_system_app.models import Attendance, Subject, SessionYear, Student, AttendanceReport


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
def manage_attendances(request):
    attendances = Attendance.objects.all()
    return render(request, 'student_management_system_app/staff_template/manage_attendances.html', {"attendances":attendances})


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
        # return redirect('student_management_system_app:manage_attendances')
        return redirect('student_management_system_app:edit_attendance', instance.pk)


class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = Attendance
    template_name = 'student_management_system_app/staff_template/delete_attendance.html'
    success_url = reverse_lazy('student_management_system_app:manage_attendances')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Successfully Deleted Attendance")
        return super().delete(self, request, *args, **kwargs)

