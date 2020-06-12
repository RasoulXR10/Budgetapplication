from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # save data in database in form model
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'{username}, Your account has been created, now you can Login and Add Project!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'budget/profile.html', {'title': 'Profile'})
