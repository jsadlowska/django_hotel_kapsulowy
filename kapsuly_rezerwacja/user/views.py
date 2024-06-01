from django.shortcuts import render, redirect
from user.forms import SignUpForm

def signup(response):
    if response.method == 'POST':
        form = SignUpForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('index.html')
    else:
        form = SignUpForm()
    return render(response, "signup.html",{"form":form})

