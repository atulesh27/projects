from django.shortcuts import render
from .forms import user_form
from .forms import StudentRegistration

def reg_form_view(r):
    form = user_form()
    if r.method == 'POST':
        form = user_form(r.POST)
        if form.is_valid():
            form.save()
    my_dict = {'form':form}
    return render(r,'app_25/form.html',context=my_dict)

def show_from_data(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('form validation')
            print('name:', fm.cleaned_data['name'])
            print('email:', fm.cleaned_data['email'])
    else:
        fm = StudentRegistration()

    return render(request, 'app_25/userregistration.html', {'fm': fm})
