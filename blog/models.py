from django.db import models
COMMUNITY_CHOICES = (
        ('C1', '미국'),
        ('C2', '일본'),
        ('C3', '캐나다'),
    )


class Blog(models.Model):
    title = models.CharField(max_length=200) #제한 있음.
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField() #제한 없음.
    image = models.ImageField(upload_to="blog/", blank=True, null=True )
    community = models.CharField(max_length=100, choices=COMMUNITY_CHOICES,default="C1")
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #파이썬 리스트 슬라이싱

