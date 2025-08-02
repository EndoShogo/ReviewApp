from django.db  import models
from django.contrib.auth.models import User
from django.utils import timezone

class ReviewModel(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)   #レビューするユーザー
    title = models.CharField(max_length = 100) #レビューのタイトル  
    content = models.TextField() #レビューの内容
    useful_num= models.IntegerField(null = True,blank = True, default = 0)
    project_image = models.ImageField(upload_to='',null = True,blank=True)
    likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}のプロフィール"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.sender.username} → {self.recipient.username}: {self.subject}"

