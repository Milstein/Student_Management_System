from django.urls import path, include

# For loading Static/ Media files i.e. Image
from django.conf import settings
from django.conf.urls.static import static

from student_management_system_app import HodViews
from . import views

# My name space
app_name = 'student_management_system_app'

urlpatterns = [
    # path('demo/', views.showDemoPage),
    # path('', views.home, name='home'),
    path('', views.HomePageView.as_view(), name='home'),
    path('dologin/', views.dologin, name='dologin'),
	path('admin_home', HodViews.admin_home, name='admin_home'),
	path('add_staff', HodViews.add_staff, name='add_staff'),
	path('add_staff_save', HodViews.add_staff_save, name='add_staff_save'),
    path('get_user_details/', views.GetUserDetails, name='userdetails'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
