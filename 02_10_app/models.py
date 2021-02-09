from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# model 생성
class User(AbstractUser):
# 여기서 AbstractUser란 기존 user의 모델을 사용하여 추가나 삭제를 진행가능
    u_id = models.CharField(db_column='U_ID', max_length=20, null=True)
    uname = models.CharField(db_column='UNAME', max_length=20, null=True)
    matlab_file = models.FileField(db_column='MATLAB_FILE', null=True)  # 비워둘수도 있음

    # instance 자체를 출력시 모양을 바꿔줌
    def __str__(self):
        return self.uname  # admin 화면에서 이름을 확인할수 있음.