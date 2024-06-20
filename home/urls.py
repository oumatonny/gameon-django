from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('event/<int:event_id>/book/', views.book_event, name='book_event'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/add_comment/<int:article_id>/', views.add_comment, name='create_comment'),
    path('article/create/', views.create_article, name='create_article'),
    path('event/create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/update/', views.update_event, name='update_event'),
    path('live/create/', views.create_live_event, name='create_live_event'),
    path('live/<int:live_event_id>/', views.live_event_detail, name='live_event_detail'),
    path('photo/create/', views.create_photo, name='create_photo'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('comment/<int:comment_id>/feedback/', views.comment_feedback, name='comment_feedback'),
    path('articles/', views.articles, name='articles'),
    path('events/', views.events, name='events'),
    path('live-events/', views.live_events, name='live_events'),    
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('comments/', views.comments, name='comments'),
    path('photos/', views.photos, name='photos'),
    path('article/<int:article_id>/comment/', views.add_comment, name='create_comment'),
    path('article/<int:article_id>/feedback/', views.create_feedback, name='create_feedback'),
]