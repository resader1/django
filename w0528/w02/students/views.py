from django.shortcuts import render
from students.models import Student

# Create your views here.

def write(request):
    return render(request,'write.html')


def view(request):
    return render(request,'view.html')


def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)