from django.shortcuts import render


# Create your views here.

# create a function
def simple_view(request):
    data = {"content": "Gfg is the best"}
    return render(request, "car/geeks.html", data)

#
def check_age(request):
    if request.method == 'POST':
      # Get the age from the form
        age = int(request.POST.get('age', 0))
        return render(request, 'car/check_age.html', {'age': age})
    return render(request, 'car/check_age.html')

# filtering number which divisible by 2

def loop(request):
    data = "Gfg is the best"
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {
        "data": data,
        "list": number_list}

    return render(request, "car/loop.html", context)


#index information::
def index(r):
    return render(r, 'car/index.html')

