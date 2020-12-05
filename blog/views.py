from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'Blog post Content',
        'date_posted': '4th December 2020'
    },
    {
        'author': 'Kousik',
        'title': 'Blog post 2',
        'content': 'Blog post Content',
        'date_posted': '4th December 2020'
    }
]

def home(request):
    """ Blog home """
    context = {
        'posts': posts
    }
    # return HttpResponse('<h1>Blog home</h1>')
    return render(request, template_name='blog/home.html', context=context)

def about(request):
    """ Blog about page """
    return render(request, template_name='blog/about.html', context={'title':'about'})