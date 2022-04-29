from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User




class Post(models.Model):
    title=models.CharField(max_length=255)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255,default="The Post")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    follow= models.ManyToManyField(User,related_name='Twitt_posts')
    def __str__(self):
        return self.title + '|'+ str(self.author)

    def total_likes(self):
        return self.follow.count()
    def get_absolute_url(self):
        return reverse('article_detail',args=(str(self.id)))
