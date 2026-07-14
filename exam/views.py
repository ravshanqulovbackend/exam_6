from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from django.contrib import messages  
from .models import Post, Category, Comment

def home_page(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.annotate(post_count=Count('posts'))

    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query))

    cat_id = request.GET.get('category')
    if cat_id:
        posts = posts.filter(category_id=cat_id)

    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog.html', context)

def single_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categories = Category.objects.annotate(post_count=Count('posts'))
    comments = post.comments.all()
    comments_count = comments.count()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')

        if name and email and body:
            Comment.objects.create(
                post=post,
                name=name,
                email=email,
                body=body
            )
            messages.success(request, "Izoh muvaffaqiyatli saqlandi!")
            return redirect('single', pk=post.pk)
        else:
            messages.error(request, "Xatolik yuz berdi! Iltimos, qaytadan urinib ko'ring.")

    context = {
        'post': post,
        'categories': categories,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'single.html', context)