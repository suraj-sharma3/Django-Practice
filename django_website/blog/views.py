from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>") # We can also view this HTML code when we go to blog home page and click on view page source

# def about(request):
#     return HttpResponse("<h1>Blog About</h1><p>This is the about page of the blog</p><br><hr>") # The entire HTML code of a website can be passed as a string here but that would the make the code very cluttered, that's why we use templates for HTML

# We have to create a templates folder within the blog app which should contain another folder named blog which will contain all the HTML templates

posts = [
    {
        "author": "John Doe",
        "title": "Understanding Python Basics",
        "content": "This post covers the fundamentals of Python programming, including data types, control structures, and functions.",
        "date_posted": "2024-12-10"
    },
    {
        "author": "Jane Smith",
        "title": "Advanced Machine Learning Techniques",
        "content": "An in-depth look at machine learning algorithms, with a focus on neural networks and deep learning.",
        "date_posted": "2024-12-08"
    },
    {
        "author": "Alice Brown",
        "title": "Introduction to Data Science",
        "content": "This post provides a comprehensive overview of data science, covering data analysis, visualization, and machine learning.",
        "date_posted": "2024-12-05"
    }
]

def home(request):
    context = {'posts' : posts} # the value is the posts list from above
    return render(request, "blog/home.html", context) # the first parameter of the render function is the request received by the home view function and second parameter is the path to the template which contains the directory name from templates folder and the name of the template, the third parameter context contains the list of all the posts which will be now available on the home page of the blog app
    # passing the context dictionary to the render function provides the HTML code or template of home page access to this dictionary that contains the list of posts

def about(request):
    return render(request, "blog/about.html", {'title' : 'About Page'})

# Below given jinja code will be included in home.html : 

# {% Python code %} is used to start and end any python code block in html with jinja 

# {{ Variable name }} is used to use any python variable within a python code block in html with jinja 

# {% Python code %} is used to end any python code block in html with jinja, here we are ending the for loop, a similar approach is used for while, if, etc 