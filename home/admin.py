from django.contrib import admin
from .models import Article, Event, Booking, Comment, Live, Photo, Feedback

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'user')
    search_fields = ('name', 'user__username')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp')
    search_fields = ('user__username', 'event__name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at')
    search_fields = ('user__username', 'article__title')

class LiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('comment', 'created_at')
    search_fields = ('comment__content',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Live, LiveAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Feedback, FeedbackAdmin)
