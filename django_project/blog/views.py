from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'CoreyMs',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'Aug 14,2025'
    },
    {
        'author':'Abhirup',
        'title':'Blog post 2',
        'content':'First post content',
        'date_posted':'Aug 14,2025'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'Django-About'})