from django.shortcuts import render, redirect
from user.forms import SignUpForm
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password = raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print('Uwierzytelnienie nie powiodło się')
        else:
            print("Formularz jest niepoprawny", form.errors)
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})






