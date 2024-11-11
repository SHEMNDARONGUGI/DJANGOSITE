
from django.contrib import admin
from django.urls import path
from Smart_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home),
    path('about/', views.about),
    path('register/', views.register),
    path('contact/', views.contact),
    # path('courses/', views.course),
    path('faq/', views.faq),
    path('login/', views.login),
]
