from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    body_image = models.ImageField(upload_to='blog',null=True)
    pub_data = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    user_detail = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def summary(self):
        return self.body[:300]

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    user_detail = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_detail = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user_detail = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_detail = models.ForeignKey(Blog,on_delete=models.CASCADE)

class User_Details(models.Model):
    fname = models.CharField(max_length=15,null=True)
    mname = models.CharField(max_length=15,null=True)
    lname = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=50,null=True)
    phone_no = models.IntegerField(default=0,null=True)
    email_id = models.CharField(max_length=25,null=True)
    user_link = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/',null=True)

    @property
    def fullname(self):
        if (self.fname=='None' or self.fname==None) and (self.mname=='None' or self.mname==None) and (self.lname=='None' or self.lname==None):
            return self.user_link.username
        elif (self.fname!='None' or self.fname!=None) and (self.mname=='None' or self.mname==None) and (self.lname=='None' or self.lname==None):
            return self.fname
        elif (self.fname!='None' or self.fname!=None) and (self.mname=='None' or self.mname==None) and (self.lname!='None' or self.lname!=None):
            a = self.fname + ' ' + self.lname
            return a
        else:
            a = self.fname + ' ' + self.mname + ' ' + self.lname
            return a

    def __str__(self):
        return self.fname