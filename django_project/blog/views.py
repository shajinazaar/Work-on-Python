from django.shortcuts import render
from .models import Post #importing Post class from models file
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
#from django.views.generic.detail import DetailView
#from django.http import HttpResponse
# Create your views here.

posts=[
    {
    'author':'Shaji Nazar',
    'title':'Blog Post 1',
    'content':'First post content',
    'date_posted':'Nov 5,2019'

    },
    {
    'author':'Jane Doe',
    'title':'Blog Post 2',
    'content':'Second post content',
    'date_posted':'Nov 6,2019'

    }

] #Creating list of dictionary for dummy data

def Home(request):
    context={
    'posts':Post.objects.all()

    }
    return render(request,'blog/Home.html',context)

    #return HttpResponse('<h1>Blog home</h1>')

#Creating class based view i.e ListView which show all the posts
class PostListView(ListView):
    model= Post
    template_name ='blog/Home.html'  # <app> /<model> _<viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_posted']
# Creating view for an indiviual post
class PostDetailView(DetailView):
    model=Post
#Creating a form for the post
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields =['title','content']
#form_valid() used get_absolute_url() method
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
#UserPassesTestMixin WILL run this test_func function, which check that if user passes certain conditions
    def test_func(self):
        post=self.get_object()  #We are using UpdateView method get_object() to get the exact post which want to UpdateView
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post

    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


def About(request):

    #return HttpResponse('<h1>Blog about</h1>')
    return render(request,'blog/About.html',{'title':'About'})
