from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='sup'),
    path('signin/',views.signin,name='sin'),
    path('signout/',views.signout,name='sut'),
    #path('changepass/',views.changepassword,name='cpass'),
    path('<str:operation>/<int:uid>',views.user_friend,name="ufriend"),
]