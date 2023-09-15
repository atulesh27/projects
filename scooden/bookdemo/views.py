from django.shortcuts import render

# Create your views here.
from .models import BookDemoModel
from .forms import BookDemoForm
from django.http import HttpResponse

def BookDemoView(r):
    form = BookDemoForm()
    if r.method=='POST':
        form = BookDemoForm(r.POST)
        if form.is_vaild():
            form.save()
            return HttpResponse('/')
    return render(r,'BookDemo/demo.html',{'form':form})

