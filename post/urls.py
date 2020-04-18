from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/<int:pk>/',views.create_blog,name='create'),
    path('mypost/<int:pk>/',views.my_blog,name='mypost'),
    path('deleteblog/<int:pk>/',views.delete_blog,name="deleteblog"),
    path('comment/<int:bid>/<int:uid>/',views.post_comment,name='post_comment'),
    path('likes/<int:bid>/<int:uid>/',views.increase_like,name='likes'),
    path('update/<int:bid>/',views.update_blog,name='update'),
    path('profile/<int:uid>/',views.profile,name='profile'),
    path('updateprofile/<int:uid>',views.update_profile,name='updatep'),
    path('viewprofile/<int:uid>',views.view_profile,name='vprofile'),
]