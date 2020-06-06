from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from student_management_system_app.EmailBackEnd import EmailBackEnd
from student_management_system_app.models import CustomUser


class HomePageView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'student_management_system_app/index.html'
    context_object_name = 'users'

    # def get_queryset(self):
    #     students = super().get_queryset()
    #     return students.filter(manager=self.request.user)
    #     # return Student.objects.order_by('-date_added')[:5]


def show_login(request):
    return render(request, 'registration/login.html')


def login_user(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not allowed!</h2>")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = EmailBackEnd.authenticate(request, username=email, password=password)
    if user:
        login(request, user)
        if user.user_type=="1":
            return redirect('student_management_system_app:admin_home')
        elif user.user_type=="2":
            return redirect('student_management_system_app:staff_home')
        else:
            return redirect('student_management_system_app:student_home')
    else:
        messages.error(request, "Invalid Login Credentials!")
        return redirect('student_management_system_app:home')


@login_required
def GetUserDetails(request):
    if request.user:
        return HttpResponse("User: " + request.user.email + " User type: " + request.user.user_type)
    return HttpResponse("Please Login First!")


@login_required
def logout_user(request):
    logout(request)
    return redirect('student_management_system_app:home')


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('student_management_system_app:home')


def show_firebase_server_worker(request):
    response = 'importScripts("https://www.gstatic.com/firebasejs/7.15.0/firebase-app.js");' \
        'importScripts("https://www.gstatic.com/firebasejs/7.15.0/firebase-messaging.js");' \
        'const firebaseConfig = {' \
        '    apiKey: "AIzaSyDNwB2NsBw1UOH4_w3VSNNfQKH946HkT5c",' \
        '    authDomain: "studentmanagementsystem-379fd.firebaseapp.com",' \
        '    databaseURL: "https://studentmanagementsystem-379fd.firebaseio.com",' \
        '    projectId: "studentmanagementsystem-379fd",' \
        '    storageBucket: "studentmanagementsystem-379fd.appspot.com",' \
        '    messagingSenderId: "915561761420",' \
        '    appId: "1:915561761420:web:26c3c7bc8dfffbf36309a9",' \
        '    measurementId: "G-19Y529Q293"' \
        '  };' \
        'firebase.initializeApp(firebaseConfig);' \
        'const messaging = firebase.messaging();' \
        'messaging.setBackgroundMessageHandler(function(payload){' \
        '    console.log(payload);' \
        '    const notification = JSON.parse(payload);' \
        '    const notificationOptions={' \
        '      body: notification.body,' \
        '      icon: notification.icon' \
        '    };' \
        '    return self.ServiceWorkerRegistration.showNotification(notification.title, notificationOptions);' \
        '});'

    return HttpResponse(response)