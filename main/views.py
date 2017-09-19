from django.contrib import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
from django.utils import timezone
from django.db.models import Q

from main.models import Post
from main.forms import SignUp, PostForm


def post(request):
    context = {'post': Post.objects.all()}
    return render(request, "post.html", context)


def signup(request):
    context = {}
    if request.method == 'POST':
        #       pass
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()  # save in database
            return redirect('/')
        else:
            messages.error(request, 'error....')
    else:
        #        signupform = UserCreationForm()
        signupform = SignUp()
        context = {'signupform': signupform}
    return render(request, 'signup.html', context)


def update_post_likes(request):
    print(request.GET)
    post_id = request.GET.get('post_id')
    print(post_id)
    likes = 0

    if post_id:
        post = Post.objects.get(id=int(post_id))
        if post is not None:
            post.likes = post.likes + 1

            likes = post.likes
            post.save()

    return HttpResponse(likes)


def postform(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)

        if post.is_valid():
            myPost = post.save(commit=False)
            myPost.created_at = timezone.now()
            myPost.save()
            return redirect('/')

    else:  # blank form
        post = PostForm()
        context = {'form': post}
        return render(request, 'postform.html', context)


def ajax_search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            result = Post.objects.filter(
                Q(title__contains=q) | Q(text__contains=q)).order_by('created_at')
            data=serializers.serialize('json',result)
            return HttpResponse(data,'application/json')
        else:
            return HttpResponse("")
    else:
        print('not a ajax')
    return redirect('/')

def gallery(request):
    context = {'imgs': ['img1.jpg', 'img2.jpg', 'img3.jpg','img4.png','img5.jpg' ]}
    return render(request, 'gallery.html', context)



def custom_logout(request):
    context ={'title': 'custom_logout'}
    return render(request, "custom_logout.html", context)
