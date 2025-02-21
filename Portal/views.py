from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['passwd1']
        password2 = request.POST['passwd2']
        email = request.POST['email']
        bio = request.POST['bio']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('Portal:signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('Portal:signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('Portal:signup')

        user = User.objects.create_user(username=username, password=password1, email=email)
        user.save()
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect('Portal/index.html')

    return render(request, 'Portal/signup.html')
