from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from dash.models import Type


def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             form.save()
             #  log the user in
             return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })


def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            #login

            user = form.get_user()
            login(request,user)

            currentType = Type.objects.get(userName=user.username).userType

            if currentType=='admin':
                return redirect('dash:admin_dash')

            elif currentType=='student':
                return redirect('dash:student_dash')

            elif currentType=='staff':
                return redirect('dash:staff_dash')


    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')
