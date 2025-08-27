from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField('여기', max_length=200)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '게시글'
        verbose_name_plural = '게시글 목록'


class Memo(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memos',
        verbose_name='작성자'
    )
    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용')
    is_important = models.BooleanField('중요', default=False)
    created_at = models.DateTimeField('생성일', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '메모'
        verbose_name_plural = '메모 목록'
        ordering = ['-created_at']  # 최신순 정렬
