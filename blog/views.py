# INTERNAL
from django.shortcuts import render

# LOCAL
from toolkit.mongotools import Mongodb

# EXTERNAL

# Create your views here.
def latest_post(request):
    # Blog = mongodb("blog")
    # Blog.filter({})
    context = {}
    return render(request,'blog/latest_post.html',context=context)
    
