from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faqs.html')
    
