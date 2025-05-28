from django.shortcuts import render

# Create your views here.
def stulist(request):
    return render(request,'stulist.html')