from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'webpages/login.html')
    
def editor(request):
    return render(request,'webpages/editor.html')
    
def webpage(request):
    return render(request,'webpages/editor.html')
