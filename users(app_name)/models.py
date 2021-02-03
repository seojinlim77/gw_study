from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# model 생성
class User(AbstractUser):
# 여기서 AbstractUser란 기존 user의 모델을 사용하여 추가나 삭제를 진행가능
    matlab_file = models.FileField(null=True)  # 비워둘수도 있음