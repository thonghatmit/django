from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('fuck/',views.vcl,name='vcl'),
    path('counter', views.counter,name='counter'),
    path('tho/',views.tho1,name='tho1'),
    path('tho/<str:pk>',views.tho,name='tho'),
    path('register',views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:uname>/<str:pk>',views.post, name='post'),
    path('blog/<str:pk>',views.blog,name='blog'),
    path('blog/', views.blog1, name='blog1')
    
   
]