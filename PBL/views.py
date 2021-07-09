from django.shortcuts import render

def cover(request):
    return render(request, "PBL/cover.html")

def Login(request):
    return render(request, "PBL/Login.html")
