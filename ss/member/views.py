import uuid
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import EmailForm  # forms.py에 정의된 EmailForm 가져오기

def request_email_verification(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            code = str(uuid.uuid4())

            # 세션에 저장
            request.session['verification_email'] = email
            request.session['verification_code'] = code

            # 이메일 전송
            verification_url = request.build_absolute_uri(f"/verify-email/{code}/")
            send_mail(
                subject='이메일 인증',
                message=f'다음 링크를 클릭하여 인증을 완료하세요: {verification_url}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )
            return redirect('check_your_email')  # 확인 안내 페이지로 이동
    else:
        form = EmailForm()
    return render(request, 'email_verification/request.html', {'form': form})

def verify_email(request, code):
    session_code = request.session.get('verification_code')
    if code == session_code:
        request.session['email_verified'] = True
        return HttpResponse("이메일 인증이 완료되었습니다.")
    return HttpResponse("유효하지 않은 인증 코드입니다.")

def check_your_email(request):
    return HttpResponse("이메일을 확인하고 인증 링크를 클릭해주세요.")