#django-admin startproject flipkart
#python manage.py startapp cloths

"""django-admin startproject scooden
python manage.py startapp python_course """

#djnago-admin startproject scooden
#python manage.py startapp python_course

""" TEMPLATE_DIR = Path.joinpath(BASE_DIR,'templates')
'DIRS' = [TEMPLATE_DIR] """

#TEMPLATE_DIR = Path.joinpath(BASE_DIR, 'template')
#register database

"""python manage.py shell
>> from django.db import connection
>> c = connection.cursor()
>> exit() """

from django.db import models

class clothmodel(models.Model):
    id = models.CharField(max_length=25)
    pattern = models.CharField(max_length=50)
    color = [('Black','Black'),('Red','Red'),('BLUE','BLUE')]
    colors = models.CharField(max_length=6,default='Black')

python manage.py makemigrations
python manage.py migrate

from django import form
from .models import clothmodel

class clothform(forms.ModelForm):
    class Meta:
        models = clothmodel
        fields = "__all__" \

class clothform(forms.ModelForm):
    class Meta:
        models = clothmodel
        fields = "__all__"

from .models import clothmodel
from .forms import clothform
from django.http import HttpResponseRedirect

#create views :

#fetch the data from database and display in frontend

def show_view(r):
    prd_list = clothmodel.objects.all()
    my_dict = {'prd_list':prd_list}
    return render(r,'cloth/index.html',context=my_dict)

#user input data

def cloth_view(r):
    form = clothform()                      #blank from
    if r.method == 'POST':                  #data store in table
        form = clothform(r.POST)             #AGAIN NEW FORM CREATE
        if  form.is_valid(): # check form is valid
            form.save()      # save in database
            return HttpResponseRedirect('hfile.html')
    return render(r,'cloth/file.html',{'form':form})


#ftech the data from databse and dsply it in front end
 def show_view(r):
     prd_list = clothmodel.objects.all()
     my_dict = {'prd_list':prd_list}
     return render(r,'cloth/file.html',context=my_dict)

 #collect user input through form and insert into database

 def cloth_view(r):
     form = clothform()
     if r.method == 'POST':
         form = clothform(r.POST)
         if form.is_valid():
             form.save()
         return HttpResponseRedirect('hfile.html')
     return render(r,'cloth/html',{'form':form})


