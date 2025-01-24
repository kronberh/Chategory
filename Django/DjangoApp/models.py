from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birthdate = models.DateField(null=True)

class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    name = models.CharField(max_length=128)
    description = models.TextField()
    icon = models.CharField(max_length=32, blank=True, default='chat-left-text-fill')
    color = models.CharField(max_length=7, default='#808080')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryPosts')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authorPosts')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likedPosts', db_table='post_likes')

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f'{self.author}: {self.content}'
    
    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    answered = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='answers')
    likes = models.ManyToManyField(User, related_name='likedComments', db_table='comment_likes')

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f'{self.author}: {self.content}'
    
    def like_count(self):
        return self.likes.count()

    def is_liked_by(self, user):
        return self.likes.filter(id=user.id).exists()
