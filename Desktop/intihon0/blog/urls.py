from django.urls import path 
from .views import HomePage,PostDatail,SignupPage,LogoutUser,loginPage,contactPage,AboutPage,category_post
#
urlpatterns=[
    path('',HomePage,name='home'),
    path('post/<int:id>/',PostDatail,name='post_detali'),
    path('signup/',SignupPage,name='signup'),
    path('logout/',LogoutUser,name="logout"),
    path('login/',loginPage,name='login'),
    path('contact/',contactPage,name='contact'),
    path('about/',AboutPage,name='about'),
    path('category/<slug:slug>/', category_post, name='category_post'),
]

