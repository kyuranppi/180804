from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # 모델을 정의하는 코드, 모델은 object의 특별한 종류다.
    # 속성 정의 / 필드마다 어떤 종류의 데이터 타입을 가지는지 정해야 함
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    