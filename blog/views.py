from django.shortcuts import render,redirect
from .models import Post,Review
from .forms import PostForm,ReviewForm




def posts(request):

    posts=Post.objects.all()
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/blog/')
        
    else:
        form=PostForm()
    
    context={
        'posts':posts,
        'form':form
        
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)
    reviews=Review.objects.filter(post=post)
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.post=post
            myform.save()
            return redirect(f'/blog/{post.slug}')
    else:
        form=ReviewForm()
    
    context={
        'post':post,
        'form':form,
        'reviews':reviews
    }
    return render(request,'blog/post_detail.html',context)

def post_delete(request,slug):
    post=Post.objects.get(slug=slug)
    post.delete()
    return redirect('/blog/')

def update_post(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form=PostForm(instance=post)
    context={
        'form':form
    }
    return render(request,'blog/update_post.html',context)
    

    
