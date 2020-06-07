from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class SessionYear(models.Model):
    # id = models.AutoField(primary_key=True)
    session_start = models.DateField()
    session_end = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return '{} TO {}'.format(self.session_start, self.session_end)
        # return ("%s TO %s" % (self.session_start, self.session_end))


class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
    user_type = models.CharField(default=1,choices=user_type_data,max_length=10)
    # gender = models.CharField(max_length=50, choices=(
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # ))


class AdminHOD(models.Model):    
    # id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staff(models.Model):    
    # id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Course(models.Model):    
    # id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    # id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course,on_delete = models.CASCADE,default=1)
    staff_id = models.ForeignKey(CustomUser,on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.subject_name


class Student(models.Model):    
    # id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser,on_delete = models.CASCADE)
    gender = models.CharField(max_length=255)
    profile_pic = models.FileField(max_length=500) # models.ImageField(upload_to = "images/", blank=False)  or FileField(upload_to='images/')
    address = models.TextField()
    course_id = models.ForeignKey(Course,on_delete = models.DO_NOTHING)
    session_year_id = models.ForeignKey(SessionYear, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StudentBulkUpload(models.Model):
  date_uploaded = models.DateTimeField(auto_now=True)
  csv_file = models.FileField(upload_to='students/bulkupload/', help_text="Please upload your data after checking for proper formatting")


class Attendance(models.Model):    
    # id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    session_year_id = models.ForeignKey(SessionYear, on_delete = models.CASCADE)
    attendance_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceReport(models.Model):    
    # id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete = models.DO_NOTHING)
    attendance_id = models.ForeignKey(Attendance,on_delete = models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportStudent(models.Model):    
    # id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete = models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_reason = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportStaff(models.Model):    
    # id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_reason = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):    
    # id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    feedback_message = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def get_absolute_url(self):
        # return reverse("listing:detail", kwargs={'pk': self.id})
        return reverse("student_management_system_app:detail", kwargs={'pk': self.id, 'slug': self.slug})


class FeedBackStaff(models.Model):    
    # id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    feedback_message = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStaff(models.Model):    
    # id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStudent(models.Model):    
    # id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type == 2:
            Staff.objects.create(admin=instance,address='')
        if instance.user_type == 3:
            Student.objects.create(admin=instance,course_id=Course.objects.first(),session_year_id=SessionYear.objects.first(),address='',profile_pic='',gender='')

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.staff.save()
    if instance.user_type == 3:
        instance.student.save()
    

    

    

