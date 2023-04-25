from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Main page',
        'values':['First', 'Second', 'Third'],
        'obj':{
            'car': 'BMV',
            'age':10,
            'hobby':'cooking'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


