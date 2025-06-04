from django.shortcuts import render
from member.models import Member
# Create your views here.

#로그아웃 부분
def logout(request):
    # session 모두 삭제
    request.session.clear()
    context = {'msg':-1}
    return render(request,'member/login.html',context)


#로그인 부분
def login(request):
    if request.method == 'GET':
        return render(request,'member/login.html')
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        try:
            qs = Member.objects.get(id=id,pw=pw)
            request.session['session_id'] = qs.id
            request.session['session_nickName'] = qs.nickName
            msg = 1
        except:
            msg = 0
        
        cookie_info = request.COOKIES
        context = {'msg':msg,'cookie_info':cookie_info}
        response = render(request,'member/login.html',context)
        if cookie_val is not None:
            response.set_cookie('cookie_val',cookie_val,max_age=60*60*24)
        else:
            response.delete_cookie('cookie_val')
        return response