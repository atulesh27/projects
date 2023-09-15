from django.shortcuts import render
from .models import CourseInfoModel
from .forms import StudRegistrationForm
from django.http import  HttpResponse

# Create your views here.

#fetch data in front end

def CourseInfoView(r):
    Stud_list = CourseInfoModel.objects.all()

    return render(r,'courseinfo/course_information.html',{'Stud_list':Stud_list})

#Registration

def pythonregView(r):
    form = StudRegistrationForm
    if r.method=='POST':
        form = StudRegistrationForm(r.POST)
        if form.is_vaild():
            form.save()
            return HttpResponse('/')
    return render(r,'courseinfo/python.html',{'form':form})
