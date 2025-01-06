from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('contact/', views.contact,name="contact"),
    path('about/', views.about,name="about"),
    path('profile/', views.profile,name="profile"),
    path('course/', views.course,name="course"),
    path('prints/',views.prints,name="prints"),
    
]