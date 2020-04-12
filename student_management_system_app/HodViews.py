from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from student_management_system_app.forms import StudentCreationForm, StudentEditForm
from student_management_system_app.models import CustomUser, Course, Subject, Staff, Student


def admin_home(request):
    return render(request, 'student_management_system_app/hod_template/main_content.html')


def add_staff(request):
    return render(request, 'student_management_system_app/hod_template/add_staff.html')


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
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


def manage_staff(request):
    staffs = Staff.objects.all()
    return render(request, 'student_management_system_app/hod_template/manage_staff.html', {"staffs":staffs})


def edit_staff(request, staff_id):
    staff = Staff.objects.get(admin=staff_id)
    return render(request, 'student_management_system_app/hod_template/edit_staff.html', {"staff":staff})


def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=staff_id, username=username)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            staff_model = Staff.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request, "Successfully Edited Staff")
            return redirect('student_management_system_app:edit_staff', staff_id)
        except Exception as e:
            messages.error(request, "Failed to Edit Staff {}".format(e))
            return redirect('student_management_system_app:edit_staff', staff_id)


def add_student(request):
    form = StudentCreationForm()
    return render(request, 'student_management_system_app/hod_template/add_student.html', {"form": form})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
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
            course_id = form.cleaned_data["course"].id
            gender = form.cleaned_data["gender"]

            profile_pic = request.FILES['profile_pic']

            # FileSystemStorage fallbacks to MEDIA_ROOT when location
            # is empty, so we restore the empty value.
            # FileSystemStorage(location='/uploads') # i.e. /media/uploads/<filename>
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            # profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                        last_name=last_name, first_name=first_name, user_type=3)
                user.student.address = address
                course = Course.objects.get(id=course_id)
                user.student.course_id = course
                user.student.session_start_year = session_start
                user.student.session_end_year = session_end
                user.student.gender = gender
                user.student.profile_pic = filename
                user.save()
                messages.success(request, "Successfully Added Student")
                return redirect("student_management_system_app:add_student")
            except Exception as e:
                messages.error(request, "Failed to Add Student Errors: {}".format(e))
                # messages.error(request, "Failed to Add Student")
                return redirect("student_management_system_app:add_student")
        else:
            form = StudentCreationForm(request.POST)
            return render(request, 'student_management_system_app/hod_template/add_student.html', {"form": form})


def manage_student(request):
    students = Student.objects.all()
    return render(request, 'student_management_system_app/hod_template/manage_student.html', {"students":students})


def edit_student(request, student_id):
    # request.session['student_id']=student_id
    student = get_object_or_404(Student, admin=student_id)
    # student=Student.objects.get(admin=student_id)

    form=StudentEditForm(initial={'student_id': student_id})
    form.fields['email'].initial=student.admin.email
    form.fields['first_name'].initial=student.admin.first_name
    form.fields['last_name'].initial=student.admin.last_name
    form.fields['username'].initial=student.admin.username
    form.fields['address'].initial=student.address
    form.fields['course'].initial=student.course_id
    form.fields['gender'].initial=student.gender
    form.fields['session_start'].initial=student.session_start_year
    form.fields['session_end'].initial=student.session_end_year

    context = {
        'form': form,
        'id': student_id,
        'username': student.admin.username
    }
    
    return render(request,"student_management_system_app/hod_template/edit_student.html", context)


def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        # student_id=request.session.get("student_id")
        student_id = request.POST["student_id"]
        if student_id == None:
            return redirect("student_management_system_app:manage_student")

        form=StudentEditForm(request.POST, request.FILES)
        if form.is_valid():
            student_id=form.cleaned_data["student_id"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            session_start = form.cleaned_data["session_start"]
            session_end = form.cleaned_data["session_end"]
            course_id = form.cleaned_data["course"].id
            gender = form.cleaned_data["gender"]

            if request.FILES.get('profile_pic',False):
                profile_pic=request.FILES['profile_pic']
                fs=FileSystemStorage()
                profile_pic_url = fs.save(profile_pic.name, profile_pic)
                # filename = fs.save(profile_pic.name, profile_pic)
                # profile_pic_url = fs.url(filename)
            else:
                profile_pic_url=None

            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.username=username
                user.email=email
                user.save()

                student=Student.objects.get(admin=student_id)
                student.address=address
                student.session_start_year=session_start
                student.session_end_year=session_end
                student.gender=gender

                course=Course.objects.get(id=course_id)
                student.course_id=course
                if profile_pic_url!=None:
                    student.profile_pic=profile_pic_url
                student.save()
                # del request.session['student_id']
                messages.success(request,"Successfully Edited Student")
                return redirect("student_management_system_app:edit_student", student_id=student_id)
            except Exception as e:
                messages.error(request,"Failed to Edit Student! Errors: {}".format(e))
                return redirect("student_management_system_app:edit_student", student_id=student_id)
        else:
            form=StudentEditForm(request.POST, initial={'student_id': student_id})
            # student=Students.objects.get(admin=student_id)
            student = get_object_or_404(Student, admin=student_id)

            context = {
                'form': form,
                'id': student_id,
                'username': student.admin.username
            }
            
            return render(request,"student_management_system_app/hod_template/edit_student.html", context)
            
            
def add_course(request):
    return render(request, 'student_management_system_app/hod_template/add_course.html')


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
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


def manage_course(request):
    courses = Course.objects.all()
    return render(request, 'student_management_system_app/hod_template/manage_course.html', {"courses":courses})


def edit_course(request, course_id):
    return HttpResponse(course_id)


def add_subject(request):
    courses=Course.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"student_management_system_app/hod_template/add_subject.html",{"staffs":staffs,"courses":courses})

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Course.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subject(subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return redirect("student_management_system_app:add_subject")
        except:
            messages.error(request,"Failed to Add Subject")
            return redirect("student_management_system_app:add_subject")


def manage_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'student_management_system_app/hod_template/manage_subject.html', {"subjects":subjects})


def edit_subject(request, subject_id):
    return HttpResponse(subject_id)