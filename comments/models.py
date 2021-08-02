from django.db import models
from account.models import CustomUser
from blog.models import Blog

class Comment(models.Model):
    document = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(CustomUser,on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return (self.author.nickname if self.author else "무명")+ "의 댓글"