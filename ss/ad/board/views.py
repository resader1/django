from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request,'list.html')
def read(request):
    return render(request,'read.html')
def write(request):
    return render(request,'write.html')