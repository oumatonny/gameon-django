from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import *
from .forms import *
from gameon.settings import LIVE_EVENT_VIDEO_BASE_URL
from django.contrib import messages

def index(request):
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    articles = Article.objects.all().order_by('-created_at')
    live_events = Live.objects.all().order_by('-created_at')
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'home/index.html', {'events': events, 'articles': articles, 'live_events': live_events, 'photos': photos})

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        booking = Booking.objects.create(user=request.user, event=event)
        return redirect('home:events')
    return render(request, 'home/book_event.html', {'event': event})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('home:index')

@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all().order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()
            return redirect('home:article_detail', article_id=article.id)
    else:
        form = CommentForm()
    return render(request, 'home/article_detail.html', {'article': article, 'comments': comments, 'form': form})


@login_required
def add_comment(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user  
            comment.save()
            return redirect('home:index')
    else:
        form = CommentForm()
    return render(request, 'home/create_comment.html', {'form': form, 'article': article})

@login_required
def create_feedback(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.article = article
            feedback.save()
            return redirect('home:article_detail', article_id=article.id)
    else:
        form = FeedbackForm()
    return render(request, 'home/create_feedback.html', {'form': form, 'article': article})

@login_required()
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home:index')
    else:
        form = ArticleForm()
    return render(request, 'home/create_article.html', {'form': form})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event created successfully.')
            return redirect('home:index')
    else:
        form = EventForm()
    return render(request, 'home/create_event.html', {'form': form})

@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully.')
            return redirect('home:index')
    else:
        form = EventForm(instance=event)
    return render(request, 'home/update_event.html', {'form': form})

@login_required
# @user_passes_test(lambda u: u.admin)
def create_live_event(request):
    if request.method == 'POST':
        form = LiveForm(request.POST)
        if form.is_valid():
            live_event = form.save()
            messages.success(request, 'Live event created successfully.')
            return redirect('home:index')
    else:
        form = LiveForm()
    return render(request, 'home/create_live_event.html', {'form': form})

@login_required
def live_event_detail(request, live_event_id):
    live_event = get_object_or_404(Live, id=live_event_id)
    video_url = f"{LIVE_EVENT_VIDEO_BASE_URL}{live_event.video_ID}"
    return render(request, 'home/live_event_detail.html', {'live_event': live_event, 'video_url': video_url})

@login_required
# @user_passes_test(lambda u: u.admin)
def create_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            messages.success(request, 'Photo uploaded successfully.')
            return redirect('home:index')
    else:
        form = PhotoForm()
    return render(request, 'home/create_photo.html', {'form': form})

@login_required
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'home/photo_detail.html', {'photo': photo})

@login_required
def comment_feedback(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.comment = comment
            feedback.save()
            messages.success(request, 'Feedback submitted successfully.')
            return redirect('home:article_detail', article_id=comment.article.id)
    else:
        form = FeedbackForm()
    return render(request, 'home/comment_feedback.html', {'comment': comment, 'form': form})


@login_required
def articles(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'home/articles.html', {'articles': articles})

@login_required
def events(request):
    events = Event.objects.all()
    booked_events = Booking.objects.filter(user=request.user)
    return render(request, 'home/events.html', {'events': events, 'booked_events': booked_events})

@login_required
def live_events(request):
    live_events = Live.objects.all()
    return render(request, 'home/live_events.html', {'live_events': live_events})

@login_required
def feedbacks(request):
    feedbacks = Feedback.objects.filter(comment__article__author=request.user)
    return render(request, 'home/feedbacks.html', {'feedbacks': feedbacks})

@login_required
def comments(request):
    article = Article.objects.filter(author=request.user)
    comments = Comment.objects.filter(article__author=request.user)
    return render(request, 'home/comments.html', {'comments': comments, 'article':article})


from .models import Photo

@login_required
def photos(request):
    photos = Photo.objects.all()
    return render(request, 'home/photos.html', {'photos': photos})