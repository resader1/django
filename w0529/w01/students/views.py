from django.shortcuts import render,redirect
from students.models import Student

# Create your views here.

def update(request, no):
    if request.method == 'GET':
        qs = Student.objects.get(no=no)
        return render(request, "update.html", {'stu': qs})
    else:
        qs = Student.objects.get(no=no)
        qs.name = request.POST.get('name')
        qs.major = request.POST.get('major')
        qs.grade = request.POST.get('grade')
        qs.age = request.POST.get('age')
        qs.gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        qs.hobby = ','.join(hobby)
        qs.save()
        return redirect(f'/students/view/{qs.no}/')
# 학생정보 상세보기
def view(request,no):
    try:
        stu = Student.objects.get(no=no)
    except:
        stu = None
    print('전달 no :',no)
    return render(request,'view.html',{'stu':stu})

def write(request):
    if request.method =='GET':
        return render(request,"write.html")
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        hobby = request.POST.getlist('hobby')
        hobby = ','.join(hobby)
        Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobby,memo='등록').save()
        return redirect('/students/list/')




def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,"list.html",context)