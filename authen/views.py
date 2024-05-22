from django.shortcuts import render
from .models import user, project
from datetime import date

# Create your views here.

def signIn(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    exist = True
    if request.method == 'POST':
        if user.objects.filter(email = email, password = password).exists():
            exist = True
            user1 = user.objects.get(email = email)
            if user1.utype == 'Donor':
                current_date = date.today()
                p = project.objects.all()
                for i in p:
                    if i.end < current_date or i.target < 1:
                        i.delete()
                p = project.objects.all()
                return render(request, 'pages/donor.html', {"project" : p, "user" : user1})
            elif user1.utype == 'Creator':
                p = project.objects.filter(creator = user1)
                return render(request, 'pages/creator.html', {"user" : user1, "project" : p})
        else:
            exist = False
            return render(request, 'pages/login.html', {"exist":exist})

    return render(request, 'pages/login.html', {"exist":exist})

def signUp(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        mobile = request.POST.get('num')
        utype = request.POST.get('utype')
        data = user(fname = fname, lname = lname, email = email, password = password, mobilenum = mobile, utype = utype)
        data.save()
        return signIn(request)

    return render(request, 'pages/signup.html')

def editProject(request, title, user1):
    p = project.objects.get(title = title)
    if request.method == 'POST':
        p.title = request.POST.get('title')
        p.target = request.POST.get('target')
        p.details = request.POST.get('desc')
        p.start = request.POST.get('start')
        p.end = request.POST.get('end')
        p.save()
        obj = project.objects.filter(creator = user1)
        return render(request, 'pages/creator.html', {"user" : user1, "project" : obj})

    return render(request, 'pages/edit.html', {"project" : p})

def deleteProject(request, title, user1):
    p = project.objects.get(title = title)
    p.delete()
    obj = project.objects.filter(creator = user1)
    return render(request, 'pages/creator.html', {"user" : user1, "project" : obj})

def createProject(request, user1):
    if request.method == 'POST':
        u = user.objects.get(email = user1)
        title = request.POST.get('title')
        target = request.POST.get('target')
        details = request.POST.get('desc')
        start = request.POST.get('start')
        end = request.POST.get('end')
        date = project(title = title, target = target, details = details, start = start, end = end, creator = u)
        date.save()
        obj = project.objects.filter(creator = user1)
        return render(request, 'pages/creator.html', {"user" : user1, "project" : obj})
    return render(request, 'pages/create.html')

def showProject(request, title, user1):
    u = user.objects.get(email = user1)
    p = project.objects.get(title = title)
    return render(request, 'pages/show.html', {"project" : p, "user" : u})

def donateProject(request, title, user1):
    u = user.objects.get(email = user1)
    p = project.objects.get(title = title)
    if request.method == 'POST':
        u = user.objects.get(email = user1)
        p = project.objects.get(title = title)
        p.target = p.target-int(request.POST.get('amount'))
        p.save()
        current_date = date.today()
        p = project.objects.all()
        for i in p:
            if i.end < current_date or i.target < 1:
                i.delete()
        p = project.objects.all()
        return render(request, 'pages/donor.html', {"project" : p, "user" : user1})
    return render(request, 'pages/donate.html', {"project" : p, "user" : u})