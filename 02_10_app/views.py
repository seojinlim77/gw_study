from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

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

# html을 이용하여 화면에 출력
def dbcontext(request): # 화면에 사용자 출력
    members = User.objects.all()
    str = ''
    for member in members:
        str += "<p>1. 사용자. {} 파일명. {}<br>".format(member.username,member.matlab_file)
    return HttpResponse(str)

# json이용
#def posts(request):
 #   Posts = User.objects.filter(published_at__isnull=False).order_by('-published_at')
 #   post_list = serializers.serialize('json', Posts)
 #   return HttpResponse(post_list, content_type="text/json-comment-filtered")

# api를 이용한 serializer (사용자 화면만 보임)
@api_view(['GET'])
def user_list(request):
    usercontext = User.objects.all()  # usercontext에 User안의 모든 객체 저장.
    serializer = UserSerializer(usercontext, many=True)  # 여러개의 변수가 저장되어 있음
    return Response(serializer.data)

# 사용자 화면과 게시할 수 있는 화면도 같이 나옴
class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('u_id')  # u_id 기준으로 정렬됨
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        instance = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
