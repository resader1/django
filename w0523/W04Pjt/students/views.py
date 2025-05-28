from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def list(request):
    # templates 폴더 안에 list.html파일 존재
    return render(request,'list.html')
    # return HttpResponse('리스트 페이지 연결')

def view(request):
    # templates 폴더 안에 list.html파일 존재
    return render(request,'view.html')
    # return HttpResponse('리스트 페이지 연결')

def delete(request):
    # templates 폴더 안에 list.html파일 존재
    return render(request,'delete.html')
    # return HttpResponse('리스트 페이지 연결')

def write(request):
    # templates 폴더 안에 list.html파일 존재
    return render(request,'write.html')
    # return HttpResponse('리스트 페이지 연결')