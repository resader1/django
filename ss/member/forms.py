from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label="이메일 주소")