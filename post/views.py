from django.shortcuts import render, redirect
from .models import Blog, Comments, Like, User_Details
from .forms import BlogForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    b = Blog.objects.all().order_by('-pub_data')
    c = Comments.objects.all()
    return render(request,'home.html',{'blog':b,'com':c})

def create_blog(request, pk):
    if request.method=='POST':
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.body_image = request.FILES['image']
        blog.user_detail = User.objects.get(id=pk)
        blog.save()
        return redirect('home')
    return render(request, 'create_blog.html')

def my_blog(request,pk):
    u = User.objects.get(id=pk)
    b = Blog.objects.filter(user_detail=u)
    return render(request,'my_blog.html',{'blog':b})

def delete_blog(request,pk):
    b = Blog.objects.get(id=pk)
    c = User.objects.get(id=b.user_detail.id)
    b.delete()
    return redirect('mypost', c.id)

def post_comment(request, bid, uid):
    blog = Blog.objects.get(id=bid)
    user = User.objects.get(id=uid)
    com = Comments()
    com.comment = request.POST['c']
    com.user_detail = user
    com.blog_detail = blog
    com.save()
    return redirect('home')

def increase_like(request, bid, uid):
    blog = Blog.objects.get(id=bid)
    user = User.objects.get(id=uid)
    l = Like.objects.filter(blog_detail=blog,user_detail=user)
    if len(l)==0:
        blog.likes += 1
        blog.save()
        li = Like(user_detail=user,blog_detail=blog)
        li.save()
        return redirect('home')
    else:
        blog.likes -= 1
        blog.save()
        l[0].delete()
        return redirect('home')

def update_blog(request, bid):
    blog = Blog.objects.get(id=bid)
    if request.method=='POST':
        blog.title = request.POST['tit']
        blog.body = request.POST['bo']
        try:
            blog.body_image = request.FILES['im']
            blog.save()
        except:
            blog.save()
        return redirect('home')
    else:
        return render(request, 'update_blog.html',{'blog':blog})

def profile(request, uid):
    u = User.objects.get(id=uid)
    ud = User_Details.objects.get(user_link=u)
    return render(request, 'profile.html',{'ud':ud})

def update_profile(request, uid):
    u = User.objects.get(id=uid)
    ud = User_Details.objects.get(user_link=u)
    if request.method=='POST':
        ud.fname = request.POST['FNAME']
        ud.mname = request.POST['MNAME']
        ud.lname = request.POST['LNAME']
        ud.email_id = request.POST['uemail']
        ud.phone_no = request.POST['uphone']
        ud.address = request.POST['uaddress']
        try:
            ud.profile_pic = request.FILES['upic']
            ud.save()
        except:
            ud.save()
        return redirect('profile', uid)        
    else:
        return render(request, 'update_profile.html',{'ud':ud})

def view_profile(request, uid):
    u = User.objects.get(id=uid)
    ud = User_Details.objects.get(user_link=u)
    return render(request,'view_profile.html',{'ud':ud})