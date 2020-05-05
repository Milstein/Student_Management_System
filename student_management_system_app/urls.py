from django.urls import path, include

# For loading Static/ Media files i.e. Image
from django.conf import settings
from django.conf.urls.static import static

from student_management_system_app import AdminViews, StaffViews, StudentViews
from . import views

# My name space
app_name = 'student_management_system_app'

urlpatterns = [
    # path('demo', views.showDemoPage),    
    path('', views.HomePageView.as_view(), name='home'),
    path('show_login', views.show_login, name='show_login'),
    path('login_user', views.login_user, name='login_user'),
    path('get_user_details', views.GetUserDetails, name='userdetails'),
	path('logout_user', views.logout_user, name='logout_user'),
    path('signup/', views.SignupView.as_view(), name='signup'),

	path('admin_home', AdminViews.admin_home, name='admin_home'),
	path('add_staff', AdminViews.add_staff, name='add_staff'),
	path('add_staff_save', AdminViews.add_staff_save, name='add_staff_save'),
	path('manage_staffs', AdminViews.manage_staffs, name='manage_staffs'),
	path('edit_staff/<int:staff_id>', AdminViews.edit_staff, name='edit_staff'),
    path('edit_staff_save', AdminViews.edit_staff_save, name='edit_staff_save'),

    # path('contacts/create', views.ContactCreateView.as_view(), name='create'),
    # path('contacts/update/<int:pk>', views.ContactUpdateView.as_view(), name='update'),
    # path('contacts/delete/<int:pk>', views.ContactDeleteView.as_view(), name='delete'),

    path('add_session_year', AdminViews.SessionYearCreateView.as_view(), name='add_session_year'),
    # path('add_session_year_save', AdminViews.add_session_year_save, name='add_session_year_save'),
    path('manage_session_years', AdminViews.manage_session_years, name='manage_session_years'),
	path('edit_session_year/<int:pk>', AdminViews.SessionYearUpdateView.as_view(), name='edit_session_year'),
    # path('edit_session_year_save', AdminViews.edit_session_year_save, name='edit_session_year_save'),
    path('delete_session_year/<int:pk>', AdminViews.SessionYearDeleteView.as_view(), name='delete_session_year'),
    
    path('add_course', AdminViews.add_course, name='add_course'),
    path('add_course_save', AdminViews.add_course_save, name='add_course_save'),
    path('manage_courses', AdminViews.manage_courses, name='manage_courses'),
	path('edit_course/<int:course_id>', AdminViews.edit_course, name='edit_course'),
    path('edit_course_save', AdminViews.edit_course_save, name='edit_course_save'),

    path('add_subject', AdminViews.add_subject, name='add_subject'),
    path('add_subject_save', AdminViews.add_subject_save, name='add_subject_save'),
    path('manage_subjects', AdminViews.manage_subjects, name='manage_subjects'),
	path('edit_subject/<int:subject_id>', AdminViews.edit_subject, name='edit_subject'),
    path('edit_subject_save', AdminViews.edit_subject_save, name='edit_subject_save'),

    path('add_student', AdminViews.add_student, name='add_student'),
    path('add_student_save', AdminViews.add_student_save, name='add_student_save'),
    path('manage_students', AdminViews.manage_students, name='manage_students'),
	path('edit_student/<int:student_id>', AdminViews.edit_student, name='edit_student'),
    path('edit_student_save', AdminViews.edit_student_save, name='edit_student_save'),

    path('staff_home', StaffViews.staff_home, name='staff_home'),

    path('take_attendance', StaffViews.take_attendance, name='take_attendance'),
    path('get_students', StaffViews.get_students, name='get_students'),
    path('save_attendance_data', StaffViews.save_attendance_data, name='save_attendance_data'),
    
    path('view_attendance_reports', StaffViews.view_attendance_reports, name='view_attendance_reports'),
	path('edit_attendance', StaffViews.edit_attendance, name='edit_attendance'),
    path('get_attendance_dates', StaffViews.get_attendance_dates, name='get_attendance_dates'),
    path('get_attendance_students', StaffViews.get_attendance_students, name='get_attendance_students'),
    path('update_attendance_data', StaffViews.update_attendance_data, name='update_attendance_data'),
    
    path('staff_apply_leave', StaffViews.staff_apply_leave, name='staff_apply_leave'),
    path('staff_leave_save', StaffViews.staff_leave_save, name='staff_leave_save'),   

    path('staff_feedback', StaffViews.staff_feedback, name='staff_feedback'),
    path('staff_feedback_save', StaffViews.staff_feedback_save, name='staff_feedback_save'),

    path('student_home', StudentViews.student_home, name='student_home'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
