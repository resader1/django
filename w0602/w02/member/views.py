from django.shortcuts import render
from member.models import Member
# Create your views here.
def login(request):
    if request.method == 'GET':
        idCheck = request.COOKIES.get('idCheck','')
        context = {"save_id":idCheck}
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idCheck = request.POST.get('idCheck')
        
        try:
            qs = Member.objects.get(id=id,pw=pw)
        except:
            context = {'msg':0}
            return render(request,'member/login.html',context)
        
        
        
        request.session['session_id'] = id
        request.session['session_nickName'] = qs.nickName
        
        context = {'msg':1}
        response = render(request,'member/login.html',context)
        if idCheck != None:
            response.set_cookie('idCheck',id,max_age=60*60)
        else:
            response.delete_cookie('idCheck',id)
        return response