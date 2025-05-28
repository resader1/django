from django.shortcuts import render,redirect
from students.models import Student
# Create your views here.

# 학생정보 삭제
def delete(reqeust,name):
    print("삭제 이름 : ",name)
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list')
# 학생정보 수정
def update(request,name):
    if request.method == 'GET':
        print("학생이름 : ",name)
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request,'update.html',context)
    else:
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보 : ",name,major,grade,age,gender)
        print("request method: ",request.method)
        ## db 수정
        # 1. 회원검색
        qs = Student.objects.get(name=name)
        # 2. 회원정보수정
        qs.name = name
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        # 3. 저장
        qs.save()
        # Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        
        return redirect('/students/list/')





# 학생정보 상세보기
def view(request):
    name = request.GET.get('name')
    print("전달 이름 : ",name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'view.html',context)








def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보 : ",name,major,grade,age,gender)
        print("request method: ",request.method)
        ## Student 테이블 객체 불러오기
        ## 1. qs = 데이터
        ## qs.save()
        ### 2. 데이터.save()
        
        ## 3. create()
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        
        return redirect('/students/list/')
        # redirect 이후에는 url만 올 수 있음 
    else: # GET방식으로 들어올때
        
        print("request method: ",request.method)
        return render(request,'write.html')
        




def list(request):
    # DB 검색
    # objects.all():전체 가져오기, objects.get():해당되는것가져오기
    # objects.filter(): 검색가능 - __contains: 포함된 모든 값 출력 가능 ,,   gte: 크거나 같다 ,, gt:크다  ,, lte : 작거나 같다 ,, le:작다
    # objects.order_by() : 정렬, -정렬
    # qs = Student.objects.all() # 전체 가져오기
    qs = Student.objects.order_by('-id') # 순차정렬  ,  -  역순정렬
    context = {'list':qs,'count':100,'id':'aaa'}
    return render(request,'list.html',context)