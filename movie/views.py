from users.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Director, Movie
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages

# Create your views here.

def home(request):

    keyword = ''

    if request.GET.get('keyword'):
        keyword = request.GET.get('keyword')

    movies = Movie.objects.distinct().filter(Q(name__icontains=keyword) | Q(des__icontains=keyword))

    paginator = Paginator(movies, 4)
    page = request.GET.get('page')

    try:
        paged_movies = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        paged_movies = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        paged_movies = paginator.page(page)



    context = {
        'movies':paged_movies,
        'keyword':keyword,
    }
    
    return render(request, 'home.html', context)

def detail(request, slug):
    

    movie_detail = Movie.objects.get(slug=slug)

    

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie_comment = movie_detail
            comment.user = request.user.profile
            comment.save()
        
            messages.success(request, 'Your was commented')
            return redirect('detail', slug=movie_detail.slug)


    comment = movie_detail.commentMovie.all()
        
        

    context = {
        'movie_detail':movie_detail,
        'comment':comment,
        'form':form,
    }

    return render(request, 'detail.html', context)

def director(request, slug):

    director = Director.objects.get(slug=slug)


    context = {
        'director':director,
    }

    return render(request, 'director.html', context)

# def search(request):

#     if 'keyword' in request.GET:
#         keyword = request.GET['keyword']
#         if 'keyword':
#             movie = Movie.objects.order_by('-created').filter(Q(name__icontains=keyword) | Q(des__icontains=keyword))


#     paginator = Paginator(movie, 4)
#     page = request.GET.get('page')

#     try:
#         paged_movies = paginator.page(page)
#     except PageNotAnInteger:
#         page = 1
#         paged_movies = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         paged_movies = paginator.page(page)



#     context = {
#         'movie':paged_movies,
#     }
    
#     return render(request, 'search.html', context)
