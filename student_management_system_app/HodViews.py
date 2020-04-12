from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from student_management_system_app.forms import StudentCreationForm
from student_management_system_app.models import CustomUser, Course


def admin_home(request):
    return render(request, 'student_management_system_app/hod_template/main_content.html')


def add_staff(request):
    return render(request, 'student_management_system_app/hod_template/add_staff.html')


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.staff.address = address
            user.save()
            messages.success(request, "Successfully Added Staff")
            return redirect('student_management_system_app:add_staff')
        except:
            messages.error(request, "Failed to Add Staff")
            return redirect('student_management_system_app:add_staff')


def add_course(request):
    return render(request, 'student_management_system_app/hod_template/add_course.html')


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Course(course_name=course)
            course_model.save()
            messages.success(request, "Successfully Added Course")
            return redirect('student_management_system_app:add_course')
        except:
            messages.error(request, "Failed To Add Course")
            return redirect('student_management_system_app:add_course')

def add_student(request):
    form = StudentCreationForm()
    return render(request, 'student_management_system_app/hod_template/add_student.html', {"form": form})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        form = StudentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]
            course_id = form.cleaned_data["course"]
            gender = form.cleaned_data["gender"]

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                        last_name=last_name, first_name=first_name, user_type=3)
                user.student.address = address
                # course_obj = Course.objects.get(id=course_id)
                user.student.course_id = course_id
                user.student.session_start_year = session_start
                user.student.session_end_year = session_end
                user.student.gender = gender
                user.student.profile_pic = profile_pic_url
                user.save()
                messages.success(request, "Successfully Added Student")
                return HttpResponseRedirect(reverse("student_management_system_app:add_student"))
            except:
                messages.error(request, "Failed to Add Student")
                return HttpResponseRedirect(reverse("student_management_system_app:add_student"))
        else:
            form = StudentCreationForm(request.POST)
            return render(request, 'student_management_system_app/hod_template/add_student_template.html', {"form": form})