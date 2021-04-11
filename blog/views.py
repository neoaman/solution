# INTERNAL
from django.shortcuts import render

# LOCAL
from toolkit.mongotools import Mongodb

# EXTERNAL

# Create your views here.
def latest_post(request,page=0):
    c_page = int(page)
    Blog = Mongodb("blog")
    limit = 9
    query = {}
    count = Blog.filter(query=query).count()
    pages = -(-count//limit)
    skips = {i:i*limit for i in range(pages) if i*limit < count}
    output = [i for i in Blog.filter({},limit=limit,projection={"content":0},skip=c_page*limit)]
    context = {"output":output,"pages":skips,"current_p": c_page,"limit":limit}
    return render(request,'blog/latest_post.html',context=context)

def specificPost(request,postId=1):
    c_page = 0
    Blog = Mongodb("blog")
    limit = 10
    query = {}
    count = Blog.filter(query=query).count()
    pages = count//limit
    skips = {i:i*limit for i in range(pages) if i*limit < count}
    query = {"postId":postId}
    output = [i for i in Blog.filter(query,projection={"postId":0,"_id":0})]
    context = {"output":output,"pages":skips,"current_p": c_page}
    return render(request,'blog/specific_post.html',context=context)


    
