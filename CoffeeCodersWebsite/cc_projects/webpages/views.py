from django.shortcuts import render
from .models import Webpages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        next = request.POST.get('next')
        if password != "council":
            return HttpResponseRedirect('/webpages')
        print(password, next)
        if next == "create":
            webpage_name = request.POST.get('webpage_name')
            render_path = "webpages/websites/" + webpage_name + ".html"
            path = "webpages/templates/" + render_path
            new_webpage = Webpages(name=webpage_name, path=path, render_path=render_path)
            new_webpage.save()
            print(webpage_name)
            request.session["curr_webpage"] = webpage_name
            return HttpResponseRedirect('/webpages/editor')
        elif next == "edit":
            curr_webpage = request.POST.get('curr_webpage')
            request.session["curr_webpage"] = curr_webpage
            webpage = Webpages.objects.filter(name=curr_webpage)
            print(curr_webpage)
            return HttpResponseRedirect('/webpages/editor')


    all_webpages = Webpages.objects.all()
    print(all_webpages)
    return render(request,'webpages/login.html', {"all_webpages": all_webpages})

def editor(request):
    if request.method == "POST":
        curr_webpage = request.session["curr_webpage"]
        webpage = Webpages.objects.filter(name=curr_webpage)
        code = request.POST.get('code')
        print(code)
        with open(webpage[0].path, 'w') as file:
            file.write(code)
    curr_webpage = request.session["curr_webpage"]
    webpage = Webpages.objects.filter(name=curr_webpage)
    print(webpage, webpage[0].path)
    try:
        with open(webpage[0].path, 'r') as file:
            code = file.read()
            print(code)
    except:
        return render(request,'webpages/editor.html')
    print(code.strip())
    return render(request,'webpages/editor.html', {"code": code.strip()})

def webpage(request):
    curr_webpage = request.session["curr_webpage"]
    webpage = Webpages.objects.filter(name=curr_webpage)
    return render(request, webpage[0].render_path)
