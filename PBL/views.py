from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile

def cover(request):
    return render(request, "PBL/cover.html")

def Login(request):
    return render(request, "PBL/Login.html")

def Register(request):
    if request.method == 'POST':

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords don\'t match.')
            return render(request, "users/register.html")
            
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already associated with another username.')
            return render(request, "users/register.html")

        phone = request.POST.get('phone')

        if len(str(phone)) != 10:
            messages.error(request, 'Please enter valid phone number.')
            return render(request, "users/register.html")

        

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        year = request.POST.get('year')

        newUser = User.objects.create_user(username=fname, email=email, first_name=fname, last_name=lname, password=password1)
                                           
        profile = Profile(user=newUser, phone=phone, gender=gender, city=city, year=year)

        profile.save()
        newUser.save()

        messages.success(request, 'Account created successfully.')

        return redirect('Login')

    return render(request, "users/register.html")                

        #     data = request.post.get
        #     user = User.objects.create(username=request.email,first_name = request.firstname)
        # return render(request, "users/register.html")