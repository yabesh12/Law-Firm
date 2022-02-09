
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),   
    path('about/', views.about, name="about"), 
    path('attorneys/', views.attorneys, name="attorneys"), 
    path('practice-areas/', views.practice_areas, name="practice-areas"), 
    path('case/', views.case, name="case"), 
    path('blog/', views.blog, name="blog"),  
    path('contact/', views.contact, name="contact"),  
]
