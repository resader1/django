from django.shortcuts import render



def send(request,name,age):
    
    print("전달받은 값 : ",name,age)
    context = {"name":name,"age":age}
    return render(request,'send.html',context)
















def write(request):
    
    context = {}
    return render(request,"write.html",context)




def test(request):
    name = request.POST.get("name")
    kor = request.POST.get("kor")
    eng = request.POST.get("eng")
    total = int(kor)+int(eng)
    hobbys = request.POST.getlist("hobby")
    context = {"name":name,"kor":kor,"eng":eng,"total":total,"hobbys":hobbys}
    return render(request,"test.html",context)
    
    
    

def view(request):
    # get방식
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 정보 : ",name)
    print("나이 정보 : ",age)
    context = {"name":name,"age":age}
    return render(request,'view.html',context)



# Create your views here.
def list(request):
    #r request -> id=aaa
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    gender = request.POST.get("gender")
    phone = request.POST.get("phone")
    hobbys = request.POST.getlist("hobby")
    print("입력된 id 값 : ",id)
    print("입력된 pw 값 : ",pw)
    print("입력된 gender 값 : ",request.POST.get('gender'))
    print("입력된 phone 값 : ",request.POST.get('phone'))
    print("입력된 hobbys : ",hobbys)
    context = {"id":id,"pw":pw,"gender":gender,"phone":phone, "hobbys":hobbys}
    return render(request,'list.html',context)