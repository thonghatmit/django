from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
     messages.info(request,  'may phai dang nhap')
     return redirect('/')
def post(request,pk) :
    
     return render(request, 'post.html',{'pk':pk})
    
def post1 (request):
     messages.info(request,  'may cung phai dang nhap')
     return redirect('/')
    

