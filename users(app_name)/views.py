from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
def login_with_file(request):
    if request.method == "POST": # 정보를 받아오기
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")
    return render(request, 'users/loginwithfile.html')