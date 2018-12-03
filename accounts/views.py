from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# function to register a new user
def register(request):
    # submitting a register form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}!'.format(username))
            return redirect('home')
    # show blank register form
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})