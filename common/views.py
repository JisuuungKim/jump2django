from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST": # post 요청인 경우 화면에서 입력한 데이터로 새로운 사용자를 생성
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else: # get 요청인 경우 빈 폼과 함께 signup.html 반환 (처음)
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
