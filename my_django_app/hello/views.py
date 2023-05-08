from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post
from datetime import datetime
from django.db import models
# Create your views here.

def index(request):
    return render(request, 'index.html')
def vcl(request):
    return HttpResponse('<h1>Thỏ Peo Péo</h1>')

def counter(request):
    text= request.POST['text']
    amountOf=len(text.split())
    return render(request,'counter.html', {'amount':amountOf} )
def register(request):
    if request.method =='POST':
      username=request.POST.get('username', 'defaultUsername')
      password=request.POST.get('password', 'defaultPassword')
      password2=request.POST.get('password2', 'defaultPassword2')
      if password==password2:
          if User.objects.filter(username=username).exists():
              messages.info(request, 'username already exist')
              return redirect('register')
          else:
              user=User.objects.create_user(username=username,password=password)
              user.save()
              return redirect('login')
      else:
          messages.info(request, 'password is not the same')
          return redirect('register')
    else:
     return render(request, 'register.html')
def login(request):
    if request.method=='POST' :
        
        username=request.POST.get('username', 'defaultUsername')
        password=request.POST.get('password', 'defaultPassword')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,  'invalid')
            return redirect('login')
    else:
      return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def tho (request,pk):
    
     return render(request, 'tho.html',{'pk':pk})
    
def tho1 (request):
     messages.info(request,  'you have to log in !')
     return redirect('/')
def post(request,pk, uname) :
    post=Post.objects.get(id=pk)
    
    labelid = request.POST.get('submit')
    print(labelid)
    pk=request.user.username
    if labelid=='Delete':
        print('post delete')
        post.delete()
        return redirect('blog', pk=pk)
    

    return render(request, 'post.html', {'pk':pk,'post':post,'uname':uname})
    

def blog1(request):
    messages.info(request,  'you have to also log in !')
    return redirect('/')
def blog(request, pk):
    
    if request.method=='POST' :
     posttitle=request.POST.get('posttitle','False')
    
     postbody=request.POST.get('blogpost','False')
     postauthor=request.user.username
     pk=request.user.username
     if posttitle !='False'and postbody!='False' and request.POST.get('PostName')=='PostValue'  :
        Post.objects.create(title=posttitle,body=postbody,author=postauthor)
        return redirect( 'blog', pk=pk)
        
        
        
     
   
     

    
    

    print(request.POST.get('PostName'))
    posts=Post.objects.all()
    return render(request, 'blog.html' ,{'pk':pk, 'posts':posts})

