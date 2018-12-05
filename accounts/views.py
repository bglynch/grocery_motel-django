from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    '''Registers a new user or gets user the registration form'''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')

            user = auth.authenticate(username=user_name, password=user_password)
            auth.login(request, user)
            
            messages.success(
                request, 
                'Account created for {}!'.format(user_name)
                )
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# function to view user profile page, if user is logged in
@login_required
def my_account(request):
    return render(request, 'accounts/my-account.html')
