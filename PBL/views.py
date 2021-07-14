from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile
from .models import Post

def cover(request):
    return render(request, "PBL/cover.html")

def Login(request):
     if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(request, email=email, password=password)

        if user is not None:
            messages.error(request, 'Invalid credentials.')
            return redirect('Login')
            
        else:
            auth.login(request, user)
            return redirect('user-home')

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

        newUser = User.objects.create_user(username=email, email=email, first_name=fname, last_name=lname, password=password1)
                                           
        profile = Profile.objects.create(userId=newUser,fname=fname, lname=lname, email=email, phoneNo= phone, gender=gender, city=city, year=year,)

        profile.save()
        newUser.save()

        messages.success(request, 'Account created successfully.')

        return render(request, 'Login')
        messages.success(request, 'Account created successfully.')

    return render(request, "users/register.html")                

        #     data = request.post.get
        #     user = User.objects.create(username=request.email,first_name = request.firstname)
        # return render(request, "users/register.html")
def userHome(request):
    return render(request, 'PBL/user-home.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return render(request, 'PBL/logout.html')

def addpost(request):
    if request.method == 'POST':
        request1 = request.POST.get('request1')
        type = request.POST.get('type')

        post = Post.objects.create(request1=request1, type=type)

        post.save()

        messages.success(request, 'Request sent successfully.')

        return render(request, 'PBL/posts.html')

    return render(request, 'PBL/addpost.html')

def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    context1 = {
        'users': Profile.objects.all()
    }
    return render(request, 'PBL/posts.html', context, context1)
