from django import forms

from student_management_system_app.models import Course, SessionYear, StudentBulkUpload


class DateInput(forms.DateInput):
    input_type = "date"


class StudentCreationForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    course=forms.ModelChoiceField(label="Course",queryset=Course.objects.all(),empty_label="--- Select Course ---",widget=forms.Select(attrs={"class":"form-control"}))
    # course = forms.ModelChoiceField(queryset=Course.objects.all().values_list('course_name', flat=True))
    # course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    session_year=forms.ModelChoiceField(label="Session Year",queryset=SessionYear.objects.all(),empty_label="--- Select Session Year ---",widget=forms.Select(attrs={"class":"form-control"}))
    # session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    # session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    
    profile_pic=forms.FileField(label="Profile Picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control pt-3 pb-5"}))


class StudentEditForm(forms.Form):
    student_id=forms.CharField(widget = forms.HiddenInput(attrs={"readonly":"readonly"}))
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control", "readonly":"readonly"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    # courses=Course.objects.all()
    # course_list=[("", "--- Select Course ---"),]    
    # for course in courses:
    #     small_course=(course.id, course.course_name)
    #     course_list.append(small_course)

    gender_choice=[
        ("Male","Male"),
        ("Female","Female")
    ]
    
    course=forms.ModelChoiceField(label="Course",queryset=Course.objects.all(),empty_label="--- Select Course ---",widget=forms.Select(attrs={"class":"form-control"}))
    # course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    session_year=forms.ModelChoiceField(label="Session Year",queryset=SessionYear.objects.all(),empty_label="--- Select Session Year ---",widget=forms.Select(attrs={"class":"form-control"}))
    # session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    # session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    
    profile_pic=forms.FileField(label="Profile Picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control pt-3 pb-5"}),required=False)


class StudentBlukUploadForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control", "readonly":"readonly"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    gender_choice=[
        ("Male","Male"),
        ("Female","Female")
    ]
    
    course=forms.ModelChoiceField(label="Course",queryset=Course.objects.all(),empty_label="--- Select Course ---",widget=forms.Select(attrs={"class":"form-control"}))
    
    gender=forms.ChoiceField(label="Gender",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    
    session_year=forms.ModelChoiceField(label="Session Year",queryset=SessionYear.objects.all(),empty_label="--- Select Session Year ---",widget=forms.Select(attrs={"class":"form-control"}))

    profile_pic=forms.FileField(label="Profile Picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control pt-3 pb-5"}),required=False)


class SessionYearForm(forms.Form):
    session_start = forms.DateField(label="Session Start", widget=DateInput(attrs={"class": "form-control"}))
    session_end = forms.DateField(label="Session End", widget=DateInput(attrs={"class": "form-control"}))
    # class Meta: # this is only when forms.ModelForm is used as form (forms.ModelForm) not (forms.Form)
    #     model = SessionYear
    #     fields = ['session_start_year', 'session_end_year']


class StudentBulkUploadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentBulkUploadForm, self).__init__(*args, **kwargs)
        # change a widget attribute:
        self.fields['csv_file'].widget.attrs["class"] = 'form-control pt-3 pb-5'


    class Meta:
        model = StudentBulkUpload
        fields = ("csv_file",)
        labels = {'csv_file': 'CSV File',}
        # widgets ={
        #     'topping1': forms.Textarea
        #     # ,
        #     # 'size': forms.CheckboxSelectMultiple
        # }