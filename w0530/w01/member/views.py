from django.shortcuts import render,redirect
from member.models import Member
# Create your views here.
## 로그인 - 페이지 : GET, 로그인 - 확인 : POST
def login(request):
    if request.method == 'GET': #로그인페이지 연결
        return render(request,'member/login.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디, 패스워드 : ",id, pw)
        
        # id,pw가 있는지 확인
        try:
            ### id,pw를 모두 검색
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id # session 할당
                txt = 1 # 성공
            else:
                txt = -1 # 아이디 존재,비번 틀림
        except:
            txt = 0 # 아이디가 없음.
        
        # try:
        #     ### id,pw를 모두 검색
        #     qs = Member.objects.get(id=id,pw=pw)
        #     request.session['session_id'] = id # session 할당
        #     txt = 1 # 성공
        # except:
        #     txt = 0 # 실패
            
            
        context = {'msg':txt}
        return render(request,'member/login.html',context)
        # return redirect('/')
        
def logout(request):
    request.session.clear() # 섹션모두삭제, del request.session['session_id']
    context = {'msg':2}
    return render(request,'member/login.html',context)