from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    # 클래스를 설명하는 문구 넣기 (해당 클래스를 사용하는 곳에 마우스를 올리면 볼 수 있음)
    """Custom User Model"""

    # 상수 추가
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    # 젠더 필드에 사용할 옵션 생성
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    # 상수 추가
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    # 랭귀지 필드에 사용할 옵션 생성
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))

    # 상수 추가
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    # 커런시 필드에 사용할 옵션 생성
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # 아바타는 이미지 필드로 만들기
    avatar = models.ImageField(null=True, blank=True)
    # 최대 글자수는 10, 빈 필드도 허용하겠다!
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    # default='' or null='True'
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    # Boolean 필드는 참, 거짓으로 구성된 체크박스
    superhost = models.BooleanField(default=False)
