from django.contrib import admin

# 현 위치의 파일 경로에서 models.py라는 파일 불러오기
from . import models


# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
