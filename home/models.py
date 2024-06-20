from django.db import models
from accounts.models import User

class Article(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)
    comment_count = models.PositiveIntegerField(default=0)

class Event(models.Model):
    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='events')
    image = models.ImageField(upload_to='event_images', null=True, blank=True)
    description = models.TextField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    timestamp = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Live(models.Model):
    name = models.CharField(max_length=100, null=True)
    video_ID = models.CharField(max_length=255, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='photos')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='feedbacks')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)