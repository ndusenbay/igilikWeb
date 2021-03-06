from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news', NewsView.as_view(), name='news'),
    path('singleNews/<int:pk>', SingleNewsView.as_view(), name='singleNews'),
    path('blog', BlogView.as_view(), name='blog'),
    path('singleBlog/<int:pk>', SingleBlogView.as_view(), name='singleBlog'),
    path('myBlog', MyBlogView.as_view(), name='myBlog'),
    path('addBlog', AddBlog.as_view(), name='addBlog'),
    path('updataBlog/<int:pk>', UpdataBlog.as_view(), name='updateBlog'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('profile', ProfileView.as_view(), name='profile'),
]