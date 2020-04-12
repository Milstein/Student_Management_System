from django.urls import path, include

# For loading Static/ Media files i.e. Image
from django.conf import settings
from django.conf.urls.static import static

from student_management_system_app import HodViews
from . import views

# My name space
app_name = 'student_management_system_app'

urlpatterns = [
    # path('demo', views.showDemoPage),
    # path('', views.home, name='home'),
    path('', views.HomePageView.as_view(), name='home'),
    path('login_user', views.login_user, name='login_user'),
    path('get_user_details', views.GetUserDetails, name='userdetails'),
	path('logout_user', views.logout_user, name='logout_user'),
	path('admin_home', HodViews.admin_home, name='admin_home'),
	path('add_staff', HodViews.add_staff, name='add_staff'),
	path('add_staff_save', HodViews.add_staff_save, name='add_staff_save'),
	path('manage_staff', HodViews.manage_staff, name='manage_staff'),
	path('edit_staff/<int:staff_id>', HodViews.edit_staff, name='edit_staff'),
    path('edit_staff_save', HodViews.edit_staff_save, name='edit_staff_save'),
    path('add_student', HodViews.add_student, name='add_student'),
    path('add_student_save', HodViews.add_student_save, name='add_student_save'),
    path('manage_student', HodViews.manage_student, name='manage_student'),
	path('edit_student/<int:student_id>', HodViews.edit_student, name='edit_student'),
    path('edit_student_save', HodViews.edit_student_save, name='edit_student_save'),
    path('add_course', HodViews.add_course, name='add_course'),
    path('add_course_save', HodViews.add_course_save, name='add_course_save'),
    path('manage_course', HodViews.manage_course, name='manage_course'),
	path('edit_course/<int:course_id>', HodViews.edit_course, name='edit_course'),  
    path('add_subject', HodViews.add_subject, name='add_subject'),
    path('add_subject_save', HodViews.add_subject_save, name='add_subject_save'),
    path('manage_subject', HodViews.manage_subject, name='manage_subject'),
	path('edit_subject/<int:subject_id>', HodViews.edit_subject, name='edit_subject'),  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
