from django.shortcuts import render

# Create your views here.
def index(request):

    name = 'aiden'
    info = {
        'name' : 'aiden',
        'age' : 21
    }


    return render(request, 'myapp/index.html', {'info' : info})

