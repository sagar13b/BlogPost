#importing form
from django import forms
#import Blog and Comments from model file
from .models import Blog, Comments

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','body','body_image','user_detail')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)