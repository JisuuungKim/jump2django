from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm): #UserCreationForm을 상속받음
    email = forms.EmailField(label="이메일") #추가 필드

    class Meta:
        model = User #폼이 사용할 모델 지정
        fields = ("username", "password1", "password2", "email") #폼에서 사용할 필드 지정
